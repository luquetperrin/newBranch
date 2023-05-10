#!/usr/bin/python3

"""Defines a BaseModel which is a base class for other classes."""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Creating an Object.
        Args:
            args(tuple): all single elements passed in.
            kwargs(dict): all key/value arguments passed in.
        """

        if (kwargs is not None and kwargs != {}):
            for k, v in kwargs.items():
                if k == "created_at":
                    self.created_at = datetime.strptime(v,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.updated_at = datetime.strptime(v,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at instance."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of the instance."""
        ret_dict = self.__dict__.copy()
        ret_dict["__class__"] = type(self).__name__
        ret_dict["created_at"] = ret_dict["created_at"].isoformat()
        ret_dict["updated_at"] = ret_dict["updated_at"].isoformat()
        return ret_dict

    def __str__(self):
        """Prints the string representation of an object."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
