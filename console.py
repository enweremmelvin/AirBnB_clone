#!/usr/bin/env python3

"""
    this module contains the HBNBCommand class -> \
    a subclass of cmd.Cmd that inherits the properties of \
    it's base cmd.Cmd
"""

import re
import cmd
import json
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        interpreter with custom commands for our program
    """

    prompt = "(hbnb) "

    # create dictionary of legal classes where; \
    # key -> class name && value -> memory representation of class
    __legal_class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                    "State": State, "City": City, "Amenity": Amenity,
                    "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """
            quit the command line interface when \
            the EOF signal is sent to the program
        """

        print()
        return True

    def emptyline(self):
        """
            override the emptyline class to do nothing \
            when an empty line is returned

            by default, this method returns the result of the \
            last command entered
        """

        pass

    @staticmethod
    def convert_to_type(value):
        """
            static method for converting values entered to their \
            appropriate type -> used in do_update to change value \
            to its appropriate type
            EXPECTED TYPES: <int> <float> <str>
        """

        if '.' in value:
            try:
                value = float(value)
                return value
            except ValueError:
                pass
        else:
            try:
                value = int(value)
                return value
            except ValueError:
                pass

        return value

    @staticmethod
    def strip_quotes(string):
        """
            this method strips enclosing quotes on a string
        """

        for i in ["\"", "'"]:
            if string[0] == i:
                string = string[1:]
            if string[-1] == i:
                string = string[:-1]

        return string

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

        if arg not in list(self.__legal_class_dict):
            print("** class doesn't exist **")
            return

        # create new instance and save to JSON file
        class_name = None

        # search for class to create an instance of
        # class -> value of key that matches arg
        for key, value in self.__legal_class_dict.items():
            if arg == key:
                class_name = value
                break

        # create object of class found if class_name \
        # is not None
        if class_name:
            new_instance = class_name()
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

            if args[0] not in list(self.__legal_class_dict):
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                obj_dict = storage.all()
                obj_key = args[0] + "." + args[1]

                if obj_key not in list(obj_dict):
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

            if args[0] not in list(self.__legal_class_dict):
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
                    del (obj_dict[obj_key])
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

            if args[0] not in list(self.__legal_class_dict):
                print("** class doesn't exist **")
            else:
                for key, value in obj_dict.items():
                    if key.startswith(args[0]):
                        obj_list.append(str(value))

                print(obj_list)

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding \
            or updating attribute (save the change into the JSON file). \
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

            Usage: \
            update <class name> <id> <attribute name> "<attribute value>"

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
            # handle tuple argument passed to update
            # a tuple is only passed to update when a dictionary is \
            # used to update the class attributes; where: \
            # key -> attribute name | value -> attribute value
            if type(arg) is tuple:
                cls_key = arg[0] + "." + arg[2].strip("\"")
                cls_obj = obj_dict[cls_key]

                if arg[0] not in list(self.__legal_class_dict):
                    print("** class doesn't exist **")
                elif (not arg[2]) or (len(arg[2]) == 0):
                    print("** instance id missing **")
                elif cls_key not in list(obj_dict):
                    print("** no instance found **")
                else:
                    attr_dict = json.loads(arg[3])

                    for key, val in attr_dict.items():
                        # convert val to its appropriate type
                        val = self.convert_to_type(val)
                        cls_obj.__dict__[key] = val
                        storage.save()

                return

            args = arg.split()

            if args[0] not in list(self.__legal_class_dict):
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
                try:
                    i = 3
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
                attr = self.strip_quotes(attr)
                value = self.strip_quotes(value)

                # convert <value> value to its appropriate type
                value = self.convert_to_type(value)

                # set new attribute and save changes to JSON file
                obj.__dict__[attr] = value
                storage.save()

    def default(self, arg):
        """
            override default method of cmd.Cmd class to make \
            provisions for customs dynamic commands; eg: <class_name>.all() \
            where <class_name> is variable
        """

        # create a dictionary of recognised custom commands
        # key -> expected command; value -> memory representation of \
        # method to handle the given command
        arg_dict = {"all()": self.do_all, "count()": self.do_count}

        # create dictionary of recognised custom commands \
        # unlike the dictionary above; these commands require an \
        # argument be passed to them
        arg_param_dict = {"show": self.do_show, "destroy": self.do_destroy,
                          "update": self.do_update}

        # split commands entered; split by whitespace " "
        args = arg.split()

        # try and except block to handle when an argument is passed to update
        # as a dictionary -> eg: User.update("<class id>", \
        # "<key/val pair dict>")
        try:
            arg_group = re.search("(\w+)\.(\w+)\(\"?\'?(.*)\"?\'?,\s+(\{.*\})",
                                  arg)

            value = arg_group.group(4)
            value = value.replace("'", "\"")
            arg_group = arg_group.groups()

            arg_tuple = (arg_group[0], arg_group[1], arg_group[2], value)
            if arg_tuple[1] == "update":
                self.do_update(arg_tuple)
                return
        except:
            pass

        # below code in try statement handles commands that require arguments \
        # eg: User.show("<user id here>")
        try:
            # pull <class name; command; instance id> from the argument \
            # passed using regular expressions
            val_dict = {"cls_name": "", "cmd_name": "", "instc_id": ""}
            param = re.search(r"(\w+)\.(\w+)\(\"?\'?(.*)\"?\'?\)", arg)
            param = param.groups()
            val_dict_list = list(val_dict)

            # initialize empty strings in val_dict with matched groups \
            # from param -> regex to pick <class> <command> <instance>
            for i in range(len(val_dict_list)):
                try:
                    val_dict[val_dict_list[i]] = param[i]
                except IndexError:
                    pass

            # concatenate values passed in the parentheses to a string \
            # to be used by the do_update method
            if val_dict["cmd_name"] == "update":
                new_arg = val_dict["instc_id"]
                for i in ["\"", "'", ","]:
                    new_arg = new_arg.replace(i, "")

                attr_val = ""
                new_arg = new_arg.split()

                # concatenate multiple words passed as attribute \
                # values for the class to be updated
                for i in range(len(new_arg)):
                    if i > 1:
                        if i == 2:
                            attr_val = new_arg[i]
                        else:
                            attr_val += " " + new_arg[i]

                # enclose attribute value in quotes
                attr_val = "\"" + attr_val.strip() + "\""

                # concatenate arguments, where; new_arg[0] -> instance id \
                # new_arg[1] -> attribute name ; attr_val -> value of attribute
                new_arg = new_arg[0] + " " + new_arg[1] + " " + attr_val

                val_dict["instc_id"] = new_arg

            # check if command entered is in dictionary of "legal" \
            # commands and call the method to handle it
            if val_dict["cmd_name"] in list(arg_param_dict):
                for key, val in arg_param_dict.items():
                    if val_dict["cmd_name"] == key:
                        # concatenate parameter to pass to method
                        # <class> + " " + <instance id>

                        # strip quotes only if command is not <update> \
                        # otherwise; leave quotes as they are for proper \
                        # formatting of the attribute value field of <update>
                        if key != "update":
                            val_dict["instc_id"] = \
                                val_dict["instc_id"].strip("\"\'")

                        param = val_dict["cls_name"] + \
                            " " + val_dict["instc_id"]

                        val(param)
                        return
        except:
            pass

        # search for entered command in keys of dictionary
        for key, val in arg_dict.items():
            if args[0].endswith(key):
                class_name = ""

                if "." not in args[0]:
                    break

                for i in args[0]:
                    if i == ".":
                        break

                    class_name += i

                if len(class_name) > 0:
                    val(class_name)
                    return

        # print default error message if command entered is \
        # not recognised
        print("*** Unknown Syntax: {}".format(arg))

    def do_count(self, arg):
        """
            count the number of instances of a class
            return 0 if no instance found; otherwise \
            return number of instances found
        """

        if not arg:
            print("** class name missing **")
            return

        counter = 0
        obj_dict = storage.all()
        class_name = arg.split()[0]

        for key, value in obj_dict.items():
            if key.startswith(class_name):
                counter += 1

        print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
