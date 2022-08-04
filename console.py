#!/usr/bin/python3
"""Defines a console.
"""
# Imports
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines line-oriented command interpretor.
    Attributes:
    prompt (str): The command prompt.
    """
    # Cusrtom prompt, change default text dispalyed in command prompt
    prompt = "(hbnb) "

    def do_EOF(self, args):
        """Quit command to exit the program"""
        print("")
        return True  # Exit loop

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True  # Exit loop

    def emptyline(self):
        """Do nothing when empty line is entered"""
        # Method override called when an empty line is entered in
        # response to the prompt
        pass


if __name__ == '__main__':
    """cmdloop Repeatedly issue a prompt, accept input, parse an initial prefix
    off the received input, and dispatch to action methods, passing them the
    remainder of the line as argument.
    """
    HBNBCommand().cmdloop()  # Loop
