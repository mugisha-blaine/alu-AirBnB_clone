#!/usr/bin/python3
"""AirBnB Console Application"""

import cmd
from models.engine import name_class
from models import storage
from models import city
from models import place
from models import review
from models import state
from models import amenity
from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """AirBnB Console APP Subclass
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit CLI when `quit` is entered"""
        return True

    def do_EOF(self, arg):
        """Execute nothing for an EOF input"""
        return True

    def emptyline(self):
        """Execute nothing for an empty line command"""
        pass

    def do_create(self, args):
        """
                Creates a new instance of BaseModel
                create: create <class_name> (ex: create BaseModel)
        """

        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in name_class:
            print("** class doesn't exist **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
