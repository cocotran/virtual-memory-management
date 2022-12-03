from clock import Clock
from scheduler import Scheduler
from process import Process
from memory_manager import MemoryManager, Disk
from command import CommandManager
from threading import Lock


lock = Lock()

mm = MemoryManager(2, lock)
cm = CommandManager(["Store 1 5", "Store 2 3", "Store 3 7", "Lookup 3", "Lookup 2", "Release 1", "Store 1 8", "Lookup 1"])

clock = Clock(0.05)
p1 = Process("1", 2000, 3000, mm, cm)
p2 = Process("2", 1000, 2000, mm, cm)
p3 = Process("3", 4000, 3000, mm, cm)
s = Scheduler(clock, "s", 2, [p1, p2, p3])

clock.start()
s.start()
mm.start()
cm.start()
p1.start()
p2.start()
p3.start()

mm.clear_disk()

p1.join()
p2.join()
p3.join()
cm.join()
mm.join()
s.join()
clock.join()

# disk = Disk()
# disk.delete("3")

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

# print(mm.lookup("2"))
# print(mm.lookup("3"))
# print(mm.lookup("6"))

# mm.parse_command(5000, p1, "Store 1 5")
# mm.parse_command(6000, p1, "Store 2 3")
# mm.parse_command(7000, p1, "Store 3 123")
# mm.parse_command(8000, p1, "Store 4 2345")
# mm.parse_command(8000, p1, "Store 5 245")
# mm.parse_command(8000, p1, "Store 6 345")
# mm.parse_command(8000, p1, "Store 7 845")
# mm.parse_command(8000, p1, "Store 8 45")

# mm.parse_command(9000, p1, "Release 1")
# mm.parse_command(10000, p1, "Release 3")

# mm.parse_command(11000, p1, "Lookup 3")
# mm.parse_command(12000, p1, "Lookup 2")
# mm.parse_command(13000, p1, "Lookup 4")
# mm.parse_command(13000, p1, "Lookup 5")
