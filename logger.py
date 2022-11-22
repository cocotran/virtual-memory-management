class Logger:
    def __init__(self) -> None:
        pass

    def log_process_start(self, time, process):
        print(f"Clock: {time}, Process {process.id}: Started")

    def log_process_finish(self, time, process):
        print(f"Clock: {time}, Process {process.id}: Finished")
