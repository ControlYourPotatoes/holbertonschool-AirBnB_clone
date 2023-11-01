#!/usr/bin/python3
"""User class that inherits from BaseModel"""
from datetime import datetime
from models import base_model
import models


class User(base_model.BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor\n"""
        super().__init__(*args, **kwargs)
        models.storage.new(self)

    def __str__(self):
        """str method\n"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save method\n"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """to_dict method\n"""
        dic_copy = self.__dict__.copy()
        dic_copy['__class__'] = self.__class__.__name__
        dic_copy['created_at'] = self.created_at.isoformat()
        dic_copy['updated_at'] = self.updated_at.isoformat()
        return dic_copy
