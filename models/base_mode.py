#!/usr/bin/python3
"""
A module containing a base model for others
"""
from datetime import date, datetime
from uuid import uuid4


class BaseModel():
    """
    A class for BaseMode
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer method for BaseModel class
        Args:
            args: a pointer to non-keyworded arguments
            kwargs: a pointer to keyworded arguments
        """
        from models import storage
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        A method that represents a string representation of
        an object
        """
        cls_str = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
        return cls_str

    def save(self):
        """
        updater(if changes happen
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        A method that adds an attribute of an object to
        dictionary
        Returns:
            A dict() representation of the attribute key-value pairs
        """
        res = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                res[key] = datetime.isoformat(value)
            else:
                res[key] = value
        res["__class__"] = self.__class__.__name__
        return res
