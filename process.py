import random
from threading import Thread
from time import sleep
from memory_manager import MemoryManager
from command import CommandManager

# default constructor
class Process(Thread):
    def __init__(self, id: str, arrive_time: int, duration: int, memory_manager: MemoryManager, command_manager: CommandManager) -> None:
        Thread.__init__(self)
        # process number
        self.id = id
        # time at which the process arrives
        self.arrive_time = arrive_time
        # amount of quantum time allocated to process
        self.duration = duration
        self.memory_manager = memory_manager
        self.command_manager = command_manager
        self.internal_clock = None
        self.state = "available"
         # print thread status to console
    def __repr__(self) -> str:
        return f"Process {self.id}: {self.duration}"
           # print thread status to console
    def __str__(self) -> str:
        return f"Process {self.id}: {self.duration}"

    def execute(self, time, step=100) -> None:
        if self.state == "available":
            self.state = "unavaialble"
            running_time = random.randint(0, 10) * step
            self.internal_clock = time + running_time
        if self.internal_clock is None or self.internal_clock <= time:
            self.call_api(time)
        self.duration -= step
        # set duration to 0
    def is_done(self) -> bool:
        return self.duration == 0
          #Def to call API
    def call_api(self, time): 
        self.memory_manager.parse_command(time, self, self.command_manager.get_next_command())
        self.state = "available"