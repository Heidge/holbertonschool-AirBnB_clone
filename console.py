#!/usr/bin/python3
"""console for airbnb admin"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb)"

    def emptyline(self, arg):
        """do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        "quit command to exit the program"
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("Exit")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
