#!/usr/bin/python3

"""Defines FilrStorage class."""
import json
import os


class FileStorage:
    """It serializes and deserializes JSON file instances."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds to __objects dictionary the obj with key <obj class name>.id."""
        obj_key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            s_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(s_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(FileStorage.__file_path):
            """Checking if the file/path exists."""
            with open(FileStorage.__file_path) as f:
                ret_dict = json.load(f)
                ret_obj = {k : self.classes()[v['__class__']](**v)
                           for k, v in ret_dict.items()}
                FileStorage.__objects = ret_obj

    def classes(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {"BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
