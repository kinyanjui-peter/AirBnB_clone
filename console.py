#!/usr/bin/python3
'''Entry point of command interpreter '''

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import shlex
import datetime
from models.user import User

storage = FileStorage()
storage.reload()

List_class = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

class HBNBCommand(cmd.Cmd):
    '''definition and managing object attribute '''

    prompt = "(hbnb) "

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it 
        (to the JSON file), and prints the id'''
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in List_class:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        '''Prints the string representation of an instance
        based on the class name and id'''
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in List_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in List_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        '''Prints all string representation of all instances 
        based or not on the class name'''
        args = shlex.split(line)
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[key]) for key in all_objs])
        elif args[0] not in List_class:
            print("** class doesn't exist **")
        else:
            print([str(all_objs[key]) for key in all_objs if key.startswith(args[0])])

    def do_update(self, line):
        '''Updates an instance based on the class name and
        id by adding or updating attribute'''
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in List_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
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
            try:
                attr_value = eval(attr_value)
            except (NameError, SyntaxError):
                pass
            obj = all_objs[key]
            setattr(obj, attr_name, attr_value)
            obj.save()

    def do_help(self, arg):
        '''Get help on commands'''
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, arg):
        '''End the program'''
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
