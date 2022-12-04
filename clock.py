from time import sleep
from threading import Thread

from observable import Publisher

#class used to handle threaded clock
class Clock(Publisher, Thread):
    def __init__(self, secs=0.01, step=100) -> None:
        #Initialize the clock
        Publisher.__init__(self)
        self._secs = secs
        self._step = step
        #Set status
        self._running = False
        self.current_time = 1000
        Thread.__init__(self)
     #Run When thread.start() is called
    def run(self):
        self.dispatch(self.current_time)
        self._running = True
        while self._running:
            self.current_time += self._step
            self.dispatch(self.current_time)
            sleep(self._secs)  # for testing 

    def stop(self) -> None:
        self._running = False
