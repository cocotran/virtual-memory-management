from cmath import inf


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

    def add(self, id: str, value: str) -> None:
        if self._access_counter <= 3:  # still empty
            self.update_add_pointer()
        self.pages[self._add_pointer] = Page(id, value)
        self._access_point[self._add_pointer] = self.get_access_point()
        self.update_add_pointer()

    def delete(self, id: str) -> None:
        for i, page in enumerate(self.pages):
            if page.id == id:
                self.pages[i] = None
                self._access_point[i] = None

    def get(self, id: str) -> Page:
        for i, page in enumerate(self.pages):
            if page.id == id:
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


class MemoryManager:
    def __init__(self, page_num: int) -> None:
        self.main_memory = MainMemory(page_num)
        self.disk = Disk()

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

    def lookup(self, variable_id: str):
        var = self.main_memory.get(variable_id)
        if var == -1:
            var = self.disk.get(variable_id)
            if var != -1:
                self.disk.delete(variable_id)
                self.main_memory.add(var.id, var.value)
        return var
