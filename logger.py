class Logger:
    def __init__(self) -> None:
        pass

    def log_process_start(self, time, process):
        msg = f"Clock: {time}, Process {process.id}: Started"
        print(msg)
        self.write_to_file(msg)

    def log_process_finish(self, time, process):
        msg = f"Clock: {time}, Process {process.id}: Finished"
        print(msg)
        self.write_to_file(msg)

    def log_store_command(self, time, process, var):
        msg = f"Clock: {time}, Process {process.id}, Store: Variable {var.id}, Value: {var.value}"
        print(msg)
        self.write_to_file(msg)

    def log_lookup_command(self, time, process, var_id, var):
        result = "Not found"
        if var != -1:
            result = f"Value: {var.value}"
        msg = f"Clock: {time}, Process {process.id}, Lookup: Variable {var_id}, {result}"
        print(msg)
        self.write_to_file(msg)
    
    def log_release_command(self, time, process, var_id):
        msg = f"Clock: {time}, Process {process.id}, Release: Variable {var_id}"
        print(msg)
        self.write_to_file(msg)
    
    def log_swap_command(self, time, var1_id, var2_id):
        msg = f"Clock: {time}, Memory Manager, SWAP: Variable {var1_id} with Variable {var2_id}"
        print(msg)
        self.write_to_file(msg)

    def log_error_command(self):
        msg = f"Incorrect command!"
        print(msg)
        self.write_to_file(msg)

    def log(self, message):
        print(message)
 # write to output.txt file
    def write_to_file(self, message):
        with open("output.txt", "a") as f:
            f.write(message + "\n")
            f.close()