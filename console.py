#!/usr/bin/python3

"""Defines entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains command interpreter implements or functions."""

    prompt = '(hbnb) '

    def emptyline(self):
        """Does nothing when an empty line is entered.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it;
        """
        if line is None or line == '':
            print("** class name missing **")
        elif line not in storage.classes().keys():
            print("** class doesn't exist **")
        else:
            my_model = storage.classes()[line]()
            my_model.save()
            print(my_model.id)

    def do_show(self, line):
        """String repr of an instance based on the class name and id.
        """
        if line == '' or line is None:
            print("** class name missing **")
        else:
            str_in = line.split()
            if str_in[0] not in storage.classes().keys():
                print("** class doesn't exist **")
            elif len(str_in) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(str_in[0], str_in[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == '' or line is None:
            print("** class name missing **")
        else:
            str_in = line.split()
            if str_in[0] not in storage.classes().keys():
                print("** class doesn't exist **")
            elif len(str_in) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(str_in[0], str_in[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != '':
            str_in = line.split()
            str_in = str_in[0]
            if str_in not in storage.classes().keys():
                print("** class doesn't exist **")
            else:
                ret_list = []
                for val in storage.all().values():
                    if type(val).__name__ == str_in:
                        ret_list.append(str(val))
                print(ret_list)
        else:
            print(list(str(val) for val in storage.all().values()))

    def do_update(self, line):
        """Updates an instance.
        """
        if line != '' or line is not None:
            str_in = line.split()
            if str_in[0] not in storage.classes().keys():
                print("** class doesn't exist **")
            elif str_in[1] is None:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(str_in[0], str_in[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif str_in[2] is None:
                    print("** attribute name missing **")
                elif str_in[3] is None:
                    print("** value missing **")
                else:
                    obj = storage.all()[key]
                    str_in[3] = str_in[3].replace('"', '')
                    setattr(storage.all()[key], str_in[2], str_in[3])
                    storage.all()[key].save()
        else:
            print("** class name missing **")

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
