from clock import Clock
from scheduler import Scheduler
from process import Process
from memory_manager import MemoryManager, Disk
from command import CommandManager
from threading import Lock


def get_memconfig() -> int:
    with open("memconfig.txt", "r") as f:
        memconfig = f.readlines()
        f.close()
        return int(memconfig[0])

def get_processes(memory_manager, command_manager):
    with open("processes.txt", "r") as f:
        arr = [line.strip() for line in f.readlines()]
        f.close()
        core_num = int(arr.pop(0))
        arr.pop(0)
        arr = [p.split(" ") for p in arr]
        processes = []
        for i, process in enumerate(arr):
            processes.append(Process(i, int(process[0]) * 1000, int(process[1]) * 1000, memory_manager, command_manager))
        return core_num, processes
    
def get_commands():
    with open("commands.txt", "r") as f:
        commands = [line.strip() for line in f.readlines()]
        f.close()
        return commands

if __name__ == "__main__":

    lock = Lock()
    clock = Clock(0.05, 100)
    command_manager = CommandManager(get_commands())
    memory_manager = MemoryManager(get_memconfig(), lock)
    core_num, processes = get_processes(memory_manager, command_manager)
    scheduler = Scheduler(clock, "Scheduler", core_num, processes)

    # # memory_manager.clear_disk()   # uncomment to reset disk
    
    threads = [clock, command_manager, memory_manager, *processes, scheduler]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

