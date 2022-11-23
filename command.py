from threading import Thread


class CommandManager(Thread):
    def __init__(self, commands) -> None:
        Thread.__init__(self)
        self.commands = commands

    def get_next_command(self) -> str:
        command = self.commands.pop(0)
        self.commands.append(command)
        return command