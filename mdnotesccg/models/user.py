# -*- coding: utf-8 -*-

"""
mdnotesccg

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class User(object):

    """Implementation of the 'User' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (string): TODO: type description here.
        email (string): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "email": 'email',
        "created_at": 'created_at',
        "updated_at": 'updated_at'
    }

    def __init__(self,
                 id=None,
                 name=None,
                 email=None,
                 created_at=None,
                 updated_at=None,
                 additional_properties={}):
        """Constructor for the User class"""

        # Initialize members of the class
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        name = dictionary.get('name')
        email = dictionary.get('email')
        created_at = dictionary.get('created_at')
        updated_at = dictionary.get('updated_at')

        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]

        # Return an object of this model
        return cls(id,
                   name,
                   email,
                   created_at,
                   updated_at,
                   dictionary)
