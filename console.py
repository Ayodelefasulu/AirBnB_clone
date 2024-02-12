#!/usr/bin/python3

import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
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
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        print("Class name:", class_name)  # Debugging statement
        print("Available classes:", storage.__class__)  # Debugging statement
        if class_name not in BaseModel.__class__.__name__:
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
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.all():
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
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg and arg not in storage.all():
            print("** class doesn't exist **")
            return
        objs = storage.all().values() if not arg else \
            [v for k, v in storage.all().items() if k.split('.')[0] == arg]
        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.all():
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        setattr(obj, attr_name, attr_value)
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
