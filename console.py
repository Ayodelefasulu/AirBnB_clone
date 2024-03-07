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
import os
import json
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

    def do_create(self, arg):
        """creates a new instance of classname"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
            instance = cls()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string representation of instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        print("Class name:", class_name)  # Debugging statement
        print("Available classes:", storage.__class__)  # Debugging statement

        # if class_name not in BaseModel.__class__.__name__:
        # if not cls:
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """deletes an instance based on classname"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        print("Class name:", class_name)  # Debugging statement
        print("Available classes:", storage.__class__)  # Debugging statement

        # if class_name not in BaseModel.__class__.__name__:
        # if not cls:
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]

    def do_all(self, arg):
        """Prints all string representations of instances based on...
           the class name or without class name."""
        if arg:  # If a class name is provided
            try:
                class_name = eval(arg)  # Extract class name from argument
                instances = storage.all().values()  # Get all instances of cls
            except NameError:
                print("** class doesn't exist **")
                return
        else:  # If no class name is provided
            instances = storage.all().values()  # Get all instances of cls

        # Print string representations of the instances
        print([str(instance) for instance in instances])

    """def do_all(self, arg):
        if arg and arg not in storage.all():
            print("** class doesn't exist **")

        if not arg or arg in storage.all():
            try:
                # cls = eval(arg)
                cls = storage.all()[arg]
                print(str(storage.all().values()))
            except NameError:
                print("** class doesn't exist **")"""

    """def do_all(self, arg):
        Prints all string representations of all instances
        if arg and arg not in storage.all():
            print("** class doesn't exist **")
            return
        objs = storage.all().values() if not arg else \
            [v for k, v in storage.all().items() if k.split('.')[0] == arg]
        print([str(obj) for obj in objs])"""

    def do_update(self, arg):
        """updates an instance attribute"""
        args = arg.split()
        # cls = eval(args[0])
        keys = storage.all().keys()
        if not args[0]:
            print("** class name missing **")
            return
        if args[0]:
            try:
                cls = eval(args[0])
            except NameError:
                # if not any(cls == key.split('.')[0] for key in storage.all().keys()):
                print("** class doesn't exist **")
                return
        if not args[1]:
            print("** instance id missing **")
            return
        # if args[1] not in keys.split('.')[1]:
        # for key in keys:
        # if not any(key.split('.')[1] == args[1]\
            # for key in storage.all().keys()):
        # if args[1] not in str(keys).split('.')[1]:
        key_to_find = "{}.{}".format(args[0], args[1])
        if key_to_find not in str(storage.all().keys()):
            print("** no instance found **")
            return
        if not args[2]:
            print("** attribute name missing **")
            return
        if not args[3]:
            print("** value missing **")
            return
        instance = storage.all()[key_to_find]
        print("+++++++++++++updated+++++++++++++")
        attr_name = args[2]
        attr_value = args[3]
        # instance.args[2] = args[3]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
