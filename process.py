from threading import Thread

# default constructor
class Process(Thread):
    def __init__(self, id: str, arrive_time: int, duration: int) -> None:
        Thread.__init__(self)
        # process number
        self.id = id
        # time at which the process arrives
        self.arrive_time = arrive_time
        # amount of quantum time allocated to process
        self.duration = duration

    def __repr__(self) -> str:
        return f"Process {self.id}: {self.duration}"

    def __str__(self) -> str:
        return f"Process {self.id}: {self.duration}"

    def execute(self, step=1000) -> None:
        self.duration -= step

    def is_done(self) -> bool:
        return self.duration == 0
