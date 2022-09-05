#!/usr/bin/python3
"""
A console to run a command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter for the project
    """
    prompt = '(hbnb)'

    def emptyline(self):
        """
        makes sure nothing is executed
        """
        return False

    def do_quit(self, arg):
        """
        A command line quiter
        """
        return 1

    def do_EOF(self, arg):
        """
        A command line quiter
        """
        return 1


if __name__ == '__main__':
    HBNBCommand().cmdloop()
