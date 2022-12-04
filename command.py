from threading import Thread


class CommandManager(Thread):
    def __init__(self, commands) -> None:
         # initialize list of commands
        Thread.__init__(self)
        self.commands = commands

    def get_next_command(self) -> str:
        command = self.commands.pop(0)
        # append cmd index
        self.commands.append(command)
        # return list of commands
        return command