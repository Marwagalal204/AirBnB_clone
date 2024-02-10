#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys
from shlex import split


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def __init__(self, *args, **kwargs):
        '''Initialization'''
        super().__init__(*args, **kwargs)
        self.file_storage = FileStorage()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program by handling End-of-File (EOF)"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel", "State",
                              "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        instances = []
        if len(args) == 0:
            for obj in storage.all().values():
                instances.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in ["BaseModel", "State",
                                  "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if class_name in key:
                    instances.append(str(obj))
        print(instances)

    def do_update(self, args):
        '''Update Console instance'''
        if not args:
            print('** class name missing **')
        else:
            if split(args)[0] not in self.clsz:
                print("** class doesn't exist **")
            elif len(split(args)) < 2:
                print('** instance id missing **')
            else:
                key = "{}.{}".format(split(args)[0], split(args)[1])
                instances = storage.all()
                if key not in instances:
                    print('** no instance found **')
                elif len(split(args)) < 3:
                    print('** attribute name missing **')
                elif len(split(args)) < 4:
                    print('** value missing **')
                else:
                    setattr(instances[key], split(args)[2], split(args)[3])
                    instances[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
