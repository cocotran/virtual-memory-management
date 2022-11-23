class Logger:
    def __init__(self) -> None:
        pass

    def log_process_start(self, time, process):
        print(f"Clock: {time}, Process {process.id}: Started")

    def log_process_finish(self, time, process):
        print(f"Clock: {time}, Process {process.id}: Finished")

    def log_store_command(self, time, process, var):
        print(f"Clock: {time}, Process {process.id}, Store: Variable {var.id}, Value: {var.value}")

    def log_lookup_command(self, time, process, var_id, var):
        result = "Not found"
        if var != -1:
            result = f"Value: {var.value}"
        print(f"Clock: {time}, Process {process.id}, Lookup: Variable {var_id}, {result}")
    
    def log_release_command(self, time, process, var_id):
        print(f"Clock: {time}, Process {process.id}, Release: Variable {var_id}")
    
    def log_swap_command(self, time, var1_id, var2_id):
        print(f"Clock: {time}, Memory Manager, SWAP: Variable {var1_id} with Variable {var2_id}")

    def log_error_command(self):
        print(f"Incorrect command!")

    def log(self, message):
        print(message)