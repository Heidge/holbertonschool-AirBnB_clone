#!/usr/bin/python3
"""console for airbnb admin"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = '(hbnb)'

    def do_empty(self, arg):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("Exit")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
