#!/usr/bin/python3

"""Defines entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Contains command interpreter implements."""

    prompt = '(hbnb) '
    def emptyline(self):
        """Does nothing when an empty line is entered.
        """
        return False
    def do_EOF(self, line):
        """Gives a clean way to exit the program.
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
