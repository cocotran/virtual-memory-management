from clock import Clock
from scheduler import Scheduler
from process import Process


clock = Clock(1)
p1 = Process("1", 1, 3)
p2 = Process("2", 2, 4)
p3 = Process("3", 3, 1)
s = Scheduler(clock, "s", 1, [p1, p2, p3])

p1.start()
p2.start()
p3.start()
s.start()
clock.start()
