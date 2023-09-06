#!/usr/bin/python3
"""
  AirBnB Console Application
"""

import cmd


class HBNBCommand(cmd.Cmd):
    intro = "AirBnB CLI application!"
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
          Exit CLI when `quit` is entered
        """
        return True

    def do_EOF(self, arg):
        """ 
          Execute nothing for an EOF input
        """
        return True

    def emptyline(self):
        """ 
          Execute nothing for an empty line command
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
