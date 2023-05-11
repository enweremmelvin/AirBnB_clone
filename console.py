#!/usr/bin/env python3

"""
    this module contains the HBNBCommand class -> \
    a subclass of cmd.Cmd that inherits the properties of \
    it's base cmd.Cmd
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        interpreter with custom commands for our program
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """
            quit the command line interface when \
            the EOF signal is sent to the program
        """

        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel, saves it (to the JSON file) \
            and prints the id. Ex: $ create BaseModel

            If the class name is missing: \
            print ** class name missing ** (ex: $ create)

            If the class name doesn’t exist: \
            print ** class doesn't exist ** (ex: $ create MyModel)
        """

        if not arg:
            print("** class name missing **")
            return

        if " " in arg:
            arg = arg.split()[0]

        if arg != "BaseModel":
            print("** class doesn't exist **")
            return

        # create new instance and save to JSON file
        new_instance = BaseModel()
        storage.save()

        print(new_instance.id)

    def do_show(self, arg):
        """
            Prints the string representation of an instance based \
            on the class name and id. Ex: $ show BaseModel 1234-1234-1234

            If the class name is missing: \
            print ** class name missing ** (ex: $ show)

            If the class name doesn’t exist: \
            print ** class doesn't exist ** (ex: $ show MyModel)

            If the id is missing: \
            print ** instance id missing ** (ex: $ show BaseModel)

            If the instance of the class name doesn’t exist for the id: \
            print ** no instance found ** (ex: $ show BaseModel 121212)
        """

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_dict = storage.all()
                obj_key = args[0] + "." + args[1]

                if not obj_key in list(obj_dict):
                    print("** no instance found **")
                else:
                    obj = obj_dict[obj_key]
                    print(obj)

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id (save the \
            change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234

            If the class name is missing: \
            print ** class name missing ** (ex: $ destroy)

            If the class name doesn’t exist: \
            print ** class doesn't exist ** (ex:$ destroy MyModel)

            If the id is missing: \
            print ** instance id missing ** (ex: $ destroy BaseModel)

            If the instance of the class name doesn’t exist for the id: \
            print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_dict = storage.all()
                obj_key = args[0] + "." + args[1]

                if obj_key not in list(obj_dict):
                    print("** no instance found **")
                else:
                    # delete object and save changes to JSON file
                    del(obj_dict[obj_key])
                    storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances \
            based or not on the class name. Ex: $ all BaseModel or $ all

            The printed result must be a list of strings

            If the class name doesn’t exist: \
            print ** class doesn't exist ** (ex: $ all MyModel)
        """

        obj_list = []
        obj_dict = storage.all()

        if not arg:
            for key, value in obj_dict.items():
               obj_list.append(str(value))

            print(obj_list)
        else:
            args = arg.split()

            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key, value in obj_dict.items():
                    if key.startswith("BaseModel"):
                        obj_list.append(str(value))

                print(obj_list)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding \
            or updating attribute (save the change into the JSON file). \
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

            Usage: update <class name> <id> <attribute name> "<attribute value>"

            If the class name is missing: \
            print ** class name missing ** (ex: $ update)

            If the class name doesn’t exist: \
            print ** class doesn't exist ** (ex: $ update MyModel)

            If the id is missing: \
            print ** instance id missing ** (ex: $ update BaseModel)

            If the instance of the class name doesn’t exist for the id: \
            print ** no instance found ** (ex: $ update BaseModel 121212)

            If the attribute name is missing, print: \
            ** attribute name missing ** (ex: $ update BaseModel existing-id)

            If the value for the attribute name doesn’t exist, print: \
            ** value missing ** (ex: $ update BaseModel existing-id first_name)
        """

        obj_dict = storage.all()

        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[0] + "." + args[1] not in list(obj_dict):
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj_key = args[0] + "." + args[1]
                obj = obj_dict[obj_key]

                attr = args[2]
                value = args[3]

                # concatenate words enclosed in double quotes
                i = 3

                try:
                    new_str = ""

                    while True:
                        if i == 3 and args[i][0] == "\"":
                            new_str = args[i]
                        else:
                            new_str += " " + args[i]
                            new_str = new_str.strip()

                            if args[i][-1] == "\"":
                                break

                        i += 1

                    # set new value of <value> to new_str if \
                    # there are more than one word in the enclosed argument
                    if (len(new_str) > 0) and (new_str[-1] == "\""):
                        value = new_str
                except IndexError:
                    pass

                # strip enclosing single or double quotes
                for i in ["\"", "'"]:
                    if attr[0] == i:
                        attr = attr[1:]
                    if attr[-1] == i:
                        attr = attr[:-1]

                    if value[0] == i:
                        value = value[1:]
                    if value[-1] == i:
                        value = value[:-1]

                # convert string to int or float (if it is convertible)
                if '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        pass

                # set new attribute and save changes to JSON file
                obj.__dict__[attr] = value
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
