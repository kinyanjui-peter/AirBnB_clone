#!/usr/bin/python3

"""This script defines the HBnB console"""

import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex

"""Entry point for the HBnB console"""


class HBNBCommand(cmd.Cmd):
    """HBnB shell"""
    prompt = '(hbnb) '
    class_list = {'BaseModel': BaseModel, 'State': State, 'City': City,
                  'Amenity': Amenity, 'Place': Place, 'Review': Review,
                  'User': User}

    def emptyline(self):
        """Handles empty line"""
        pass

    def do_create(self, class_name=None):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not class_name:
            print('** class name missing **')
        elif not self.class_list.get(class_name):
            print('** class doesn\'t exist **')
        else:
            obj = self.class_list[class_name]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Shows an instance based on id"""
        class_name, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_destroy(self, arg):
        """Destroys an instance based on id"""
        class_name, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based on the class name"""
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.class_list.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.class_list.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        class_name, obj_id, attr_name, attr_val = None, None, None, None
        update_time = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            class_name = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if len(args) > 2:
            attr_name = args[2]
        if len(args) > 3:
            attr_val = list(shlex(args[3]))[0].strip('"')
        if not class_name:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not attr_name:
            print('** attribute name missing **')
        elif not attr_val:
            print('** value missing **')
        elif not self.class_list.get(class_name):
            print("** class doesn't exist **")
        else:
            key = class_name + "." + obj_id
            obj = models.storage.all().get(key)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attr_name):
                    attr_val = type(getattr(obj, attr_name))(attr_val)
                else:
                    attr_val = self.get_type(attr_val)(attr_val)
                setattr(obj, attr_name, attr_val)
                obj.updated_at = update_time
                models.storage.save()

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF to exit the program"""
        return True

    def default(self, line):
        """Handles class commands"""
        ln = line.split('.', 1)
        if len(ln) < 2:
            print('*** Unknown syntax:', ln[0])
            return False
        class_name, line = ln[0], ln[1]
        if class_name not in list(self.class_list.keys()):
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        ln = line.split('(', 1)
        if len(ln) < 2:
            print('*** Unknown syntax: {}.{}'.format(class_name, ln[0]))
            return False
        method_name, args = ln[0], ln[1].rstrip(')')
        if method_name not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(class_name, line))
            return False
        if method_name == 'all':
            self.do_all(class_name)
        elif method_name == 'count':
            print(self.count_class(class_name))
        elif method_name == 'show':
            self.do_show(class_name + " " + args.strip('"'))
        elif method_name == 'destroy':
            self.do_destroy(class_name + " " + args.strip('"'))
        elif method_name == 'update':
            lb, rb = args.find('{'), args.find('}')
            d = None
            if args[lb:rb + 1] != '':
                d = eval(args[lb:rb + 1])
            ln = args.split(',', 1)
            obj_id, args = ln[0].strip('"'), ln[1]
            if d and type(d) is dict:
                self.handle_dict(class_name, obj_id, d)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                ln = list(shlex(args))
                ln[0] = ln[0].strip('"')
                self.do_update(" ".join([class_name, obj_id, ln[0], ln[1]]))

    def handle_dict(self, class_name, obj_id, d):
        """Handles dictionary update"""
        for k, v in d.items():
            self.do_update(" ".join([class_name, obj_id, str(k), str(v)]))

    def postloop(self):
        """Prints a new line after each loop"""
        print()

    @staticmethod
    def count_class(class_name):
        """Counts the number of objects of the given class name"""
        count = 0
        for k, v in models.storage.all().items():
            if type(v).__name__ == class_name:
                count += 1
        return count

    @staticmethod
    def get_type(attr_val):
        """Returns the type of the input string"""
        try:
            int(attr_val)
            return int
        except ValueError:
            pass
        try:
            float(attr_val)
            return float
        except ValueError:
            return str


if __name__ == "__main__":
    HBNBCommand().cmdloop()
