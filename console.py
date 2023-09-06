#!/usr/bin/python3
"""AirBnB Console Application"""

import cmd
import sys
import json
from models.engine import name_class
from models import storage
from models import city
from models import place
from models import review
from models import state
from models import amenity
from models import BaseModel


def parse_args(args):
    if args:
        all_args = args.split(' ')
        return all_args
    return


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
        """Creates a new instance of BaseModel
        create: create <class_name> (ex: create BaseModel)
        """

        all_args = parse_args(args)

        if not all_args:
            print("** class name missing **")
            return
        elif all_args[0] not in name_class:
            print("** class doesn't exist **")
            return

        # create new BaseModel instance
        new_instance = BaseModel()

        # save to file.json
        storage.new(new_instance)
        storage.save()

        # print id
        print(new_instance.id)

    def complete_create(self, text, line, begidx, endidx):
        return name_class

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id
        show: show <class_name> <instance id>
        """

        all_args = parse_args(args)

        if not all_args:
            print("** class name missing **")
            return
        elif all_args[0] not in name_class:
            print("** class doesn't exist **")
            return
        elif len(all_args) < 2:
            print("** instance id missing **")
            return

        # print string rep of an instance base on class name and id
        obj_index = f'{name_class[0]}.{all_args[1]}'

        storage.reload()
        objs_in_dict = storage.all()

        try:
            obj = objs_in_dict[obj_index]
        except:
            print('** no instance found **')
        else:
            print(obj)

    def complete_show(self, text, line, begidx, endidx):
        return name_class

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        destroy: destroy <class_name> <instance id>
        """

        all_args = parse_args(args)

        if not all_args:
            print("** class name missing **")
            return
        elif all_args[0] not in name_class:
            print("** class doesn't exist **")
            return
        elif len(all_args) < 2:
            print("** instance id missing **")
            return

        # print string rep of an instance base on class name and id
        obj_index = f'{name_class[0]}.{all_args[1]}'

        storage.reload()
        objs_in_dict = storage.all()

        try:
            del objs_in_dict[obj_index]
        except:
            print('** no instance found **')
        else:
            storage.save()

    def complete_destroy(self, text, line, begidx, endidx):
        return name_class


if __name__ == "__main__":
    HBNBCommand().cmdloop()
