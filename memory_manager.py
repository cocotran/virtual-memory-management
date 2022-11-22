class Page:
    def __init__(self, id=None, value=None) -> None:
        self.id = id
        self.value = value
        self.last_access = None

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
        self._empty_page_index = None

    def has_empty_space(self) -> bool:
        for i, page in enumerate(self.pages):
            if page.is_empty():
                self._empty_page_index = i
                return True
        return False

    def add(self, id: str, value: str) -> None:
        self.pages[self._empty_page_index] = Page(id, value)

    def delete(self, id: str) -> None:
        for i, page in enumerate(self.pages):
            if page.id == id:
                self.pages[i] = None


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
        pass
