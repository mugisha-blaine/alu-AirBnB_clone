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

    def do_all(self, args):
        """Prints all string representation of all instances
        all: all [<class_name>]
        """

        all_args = parse_args(args)

        if all_args and all_args[0] not in name_class:
            print("** class doesn't exist **")
            return

        storage.reload()
        objs_in_dict = storage.all()
        objs_list = []

        for obj in objs_in_dict.values():
            objs_list.append(obj.__str__())

        print(objs_list)

    def complete_all(self, text, line, begidx, endidx):
        return name_class

    def do_update(self, args):
        """Updates an instance based on the class name and id
        update: update <class_name> <instance id> <attribute name> "<attribute value>"
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
            return

        try:
            print(obj)
            attr_name = all_args[2]
            obj_attr = obj.__dict__[attr_name]
        except KeyError:
            return
        except:
            print("** attribute name missing **")
            return
        else:
            print(obj_attr)

        try:
            attr_value = all_args[3]
        except:
            print("** value missing **")
            return
        else:
            obj.__dict__[attr_name] = attr_value
            storage.save()

    def complete_update(self, text, line, begidx, endidx):
        return name_class


if __name__ == "__main__":
    HBNBCommand().cmdloop()
