#!/usr/bin/python3
'''Entry point of command interpreter '''

import cmd
from models.engine.__init__ import storage
#importing a module

List_clas = ['amenity', 'city', 'place', 'user', 'state']

class HBNBCommand(cmd.Cmd):
    '''definition and managing object attribute '''

    prompt = "(hbnb)"

    def do_create(self, line):

        '''instane of BaseModel'''

        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show():

        '''Prints the string representation of an instance based 
                    on the class name and id '''

        if line == "" and line != "":
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
    # elif:
    #        print("** instance id missing **")
    #    else:
    #       key = "{}.{}".format(words[0], words[1])
    #       if key not in storage.all():
    #           print("** no instance found **")
    #   else:
    #           print(storage.all()[key])
    def do_destroys(self, line):
        '''Deletes an instance based on the class BaseModel and id'''
        if line == "" and line != "":

         print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
    ''' more code here'''

    def do_all(self, line):
        ''' 'Prints all string representation of all instances 
                   based or not on the class name'''
        if line == "":
            for line in self.List_class.items():
                print("\n** class doesn't exist **")

    def do_update(self, line):
        '''update object by class name and id'''
        List_classs = List_class.splitter(line)
        dictionary = models.storage.all()

        if line == "":
             print(self.List_class)
        elif line != "":
            return False
        elif len(List_class) < 2:
            return error

        else:
            exit
    
    def do_help(self, line):
        '''Get help on commands'''
        if line:
            cmd.Cmd.do_help(self, line)
        else:
            print("Documented commands (type help <topic>):")
            print("======================================== ")
            print("EOF help  quit")

    def do_prompt(self, line):
        "Change the interactive prompt"
        self.prompt = line + ': '

    def do_quit(self, line):
        '''quit command to exit the  program '''
        return True

    def do_EOF(self, line):

        '''end the program '''
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
