import os


class RenameFileCommand:
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)


class History:
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        try:
            self._commands.pop().undo()
        except AttributeError:
            pass


if __name__ == '__main__':
    history = History()
    history.execute(RenameFileCommand('/selo.lee', '/selo.doc'))
    history.execute(RenameFileCommand('/selochan.lee', '/seloro.doc'))
    history.undo()
    history.undo()