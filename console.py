#!/usr/bin/python3
'''Entry point of command interpreter '''

import cmd
#importing a module

class HBNBCommand(cmd.Cmd):
    '''definition and managing object attribute '''

    prompt = "(hbnb)"
    def do_quit(self, line):
        '''quit command to terminate the program '''
        return True
    def do_EOF(self, line):

        '''end the program '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
