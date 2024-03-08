#!/usr/bin/python3
""" This is the console engine

    Class: HBNBCommand

    Methods: create: creates a new instance of classname
             show: prints the string representation of instance
             all: prints string representation of all instance
             destroy: deletes an instance based on classname
             update: updates an instance attribute
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """This is a subclass of the Cmd superclass"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
