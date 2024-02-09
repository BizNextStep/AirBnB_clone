#!/usr/bin/python3


"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the AirBnB clone project.

    Attributes:
        id (str): A unique identifier for the BaseModel instance.
        created_at (datetime): The datetime when the BaseModel instance was created.
        updated_at (datetime): The datetime when the BaseModel instance was last updated.
    """

    def __init__(self):
        """Initialize a new BaseModel instance.

        Sets the id attribute to a unique UUID, created_at and updated_at
        attributes to the current datetime.
        """
        self.id = str(uuid.uuid4())  # Assign a unique ID using uuid.uuid4()
        self.created_at = datetime.now()  # Assign current datetime to created_at attribute
        self.updated_at = datetime.now()  # Assign current datetime to updated_at attribute

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing all attributes of the BaseModel instance
            converted to their corresponding string representation.
        """
        dict_copy = self.__dict__.copy()  # Create a copy of the instance dictionary
        dict_copy['__class__'] = self.__class__.__name__  # Add class name to dictionary
        dict_copy['created_at'] = self.created_at.isoformat()  # Convert created_at to ISO format
        dict_copy['updated_at'] = self.updated_at.isoformat()  # Convert updated_at to ISO format
        return dict_copy
