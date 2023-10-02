#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __create_key(self, obj):
        return '{}.{}'.format(obj.__class__.__name__, obj.id)

    def all(self, cls=None):
        """Returns a dictionary of all models of the specified class
        or none, if no class has been specified"""
        if cls is None:
            return FileStorage.__objects
        else:
            objects_of_class = {}

            for key, value in self.__objects.items():
                if cls == value.__class__:
                    objects_of_class[key] = value

            return objects_of_class

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[self.__create_key(obj)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes a specified object"""
        if obj is None:
            return
        else:
            delattr(self.__objects, self.__create_key(obj))
