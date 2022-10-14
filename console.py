#!/usr/bin/python3
"""console for airbnb admin"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb)"

    classes = {"BaseModel": BaseModel}

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

    def do_create(self, arg):
        """creation of new instance basemodel"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        i = 1
        args = {}
        for args in arg:
            if i == 1:
                args += arg
            elif i == 2:
                args += arg
            i += 1
        if arg == "":
            print("** class name missing **")
        elif args[1] not in self.classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            result = "{} {}".format(args[1], args[2])
            # If the instance of the class name doesn’t exist for the id, print ** no instance found ** (ex: $ show BaseModel 121212)


    def do_destroy(self, arg):
        i = 1
        args = {}
        for args in arg:
            if i == 1:
                args += arg
            elif i == 2:
                args += arg
            i += 1
        if arg == "":
            print("** class name missing **")
        elif args[1] not in self.classes:
            print("** class doesn't exist **")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
