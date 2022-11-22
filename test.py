from clock import Clock
from scheduler import Scheduler
from process import Process


clock = Clock(0.05)
p1 = Process("1", 2000, 3000)
p2 = Process("2", 1000, 2000)
p3 = Process("3", 4000, 3000)
s = Scheduler(clock, "s", 2, [p1, p2, p3])

p1.start()
p2.start()
p3.start()
s.start()
clock.start()
