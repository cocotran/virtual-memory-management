from clock import Clock
from scheduler import Scheduler
from process import Process
from memory_manager import MemoryManager, Disk


# clock = Clock(0.05)
# p1 = Process("1", 2000, 3000)
# p2 = Process("2", 1000, 2000)
# p3 = Process("3", 4000, 3000)
# s = Scheduler(clock, "s", 2, [p1, p2, p3])

# p1.start()
# p2.start()
# p3.start()
# s.start()
# clock.start()


# disk = Disk()
# disk.delete("3")

mm = MemoryManager(2)
# mm.clear_disk()

# mm.store("1", "5")
# mm.store("2", "3")
# mm.store("3", "7098")
# mm.store("4", "0")
# mm.store("5", "234")
# mm.store("6", "34")
# mm.store("7", "3")

# mm.release("3")
# mm.release("5")
# mm.release("6")

print(mm.lookup("2"))
print(mm.lookup("3"))
print(mm.lookup("6"))