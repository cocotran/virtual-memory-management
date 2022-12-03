from cmath import inf
from threading import Thread

from logger import Logger


class Page:
    def __init__(self, id=None, value=None) -> None:
        self.id = id
        self.value = value

    def __repr__(self) -> str:
        return f"{self.id} {self.value}"

    def __str__(self) -> str:
        return f"{self.id} {self.value}"

    def set(self, id: str, value: str) -> None:
        self.id = id
        self.value = value

    def is_empty(self) -> bool:
        return self.id is None and self.value is None


class MainMemory:
    def __init__(self, page_num: int) -> None:
        self.pages = [Page() for i in range(page_num)]
        self._add_pointer = None
        self._access_counter = 1
        self._access_point = [None for _ in range(page_num)]
        self.logger = Logger()

    def get_access_point(self) -> int:
        self._access_counter += 1
        return self._access_counter

    def update_add_pointer(self) -> None:
        if self.has_empty_space():
            return
        least_access_point = inf
        for i, page in enumerate(self._access_point):
            if page < least_access_point:
                self._add_pointer = i

    def has_empty_space(self) -> bool:
        for i, page in enumerate(self.pages):
            if page.is_empty():
                self._add_pointer = i
                return True
        return False

    def add(self, id: str, value: str) -> str:
        swap_id = None
        if not self.has_empty_space():
            swap_id = self.pages[self._add_pointer].id
        self.pages[self._add_pointer] = Page(id, value)
        self._access_point[self._add_pointer] = self.get_access_point()
        self.update_add_pointer()
        return swap_id

    def delete(self, id: str) -> None:
        for i, page in enumerate(self.pages):
            if page is not None and page.id == id:
                self.pages[i] = Page()
                self._access_point[i] = None

    def get(self, id: str) -> Page:
        for i, page in enumerate(self.pages):
            if page is not None and page.id == id:
                self._access_point[i] = self.get_access_point()
                self.update_add_pointer()
                return page
        return -1


class Disk:
    def __init__(self) -> None:
        self.pages_file = "vm.txt"

    def _get_pages(self, arr):
        pages = [i.split(" ") for i in arr]
        pages = [Page(i[0], i[1]) for i in pages]
        return pages

    def clear(self) -> None:
        with open(self.pages_file, "w") as f:
            f.close()

    def add(self, id: str, value: str) -> None:
        page = Page(id, value)
        with open(self.pages_file, "a") as f:
            f.write(str(page) + "\n")
            f.close()

    def delete(self, id: str) -> None:
        with open(self.pages_file, "r") as f:
            pages = self._get_pages([line.strip("\n") for line in f.readlines()])
        with open(self.pages_file, "w") as f:
            for page in pages:
                if page.id != id:
                    f.write(str(page) + "\n")
            f.close()

    def get(self, id: str) -> Page:
        with open(self.pages_file, "r") as f:
            pages = self._get_pages([line.strip("\n") for line in f.readlines()])
            f.close()
            for page in pages:
                if page.id == id:
                    return page
            return -1


class MemoryManager(Thread):
    def __init__(self, page_num: int, lock) -> None:
        Thread.__init__(self)
        self.main_memory = MainMemory(page_num)
        self.disk = Disk()
        self.logger = Logger()
        self.lock = lock

    def clear_disk(self) -> None:  # for testing
        self.disk.clear()

    def store(self, variable_id: str, value: str):
        if self.main_memory.has_empty_space():
            self.main_memory.add(variable_id, value)
        else:
            self.disk.add(variable_id, value)

    def release(self, variable_id: str):
        self.main_memory.delete(variable_id)
        self.disk.delete(variable_id)

    def lookup(self, time: int, variable_id: str):
        var = self.main_memory.get(variable_id)
        if var == -1:
            var = self.disk.get(variable_id)
            if var != -1:
                self.disk.delete(variable_id)
                swap_id = self.main_memory.add(var.id, var.value)
                if swap_id is not None:
                    self.logger.log_swap_command(time, variable_id, swap_id)
        return var

    def parse_command(self, time: int, process, command: str) -> None:
        command = command.split(" ")
        self.lock.acquire()
        if command[0] == "Store":
            if len(command) != 3:
                return
            self.store(command[1], command[2])
            self.logger.log_store_command(time, process, Page(command[1], command[2]))
        elif command[0] == "Release":
            if len(command) != 2:
                return
            self.release(command[1])
            self.logger.log_release_command(time, process, command[1])
        elif command[0] == "Lookup":
            if len(command) != 2:
                return
            var = self.lookup(time, command[1])
            self.logger.log_lookup_command(time, process, command[1], var)
        else:
            self.logger.log_error_command()
            return
        self.lock.release()
        