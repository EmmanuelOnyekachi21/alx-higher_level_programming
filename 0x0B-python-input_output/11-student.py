#!/usr/bin/python3
"""Task 11"""


class Student:
    """
    This is a `Student` class that defines a student

    Attributes:
        first_name:  FIrst name of the student.
        last_name:  LAst name of the student.
        age:  Age of the student.

    Methods:
        __init__(self, first_name, last_name, age):
            Instantiation with first_name, last_name and age.

        to_json(self): Retrieves a dictonary representation of  Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        This method initializes the first_name, last_name and age.

        Args:
            first_name: First name of student.
            last_name: Last name of student.
            age: Age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance.

        Args:
            self: Referring to the object
            attrs: List of strings to be retrieved.
        """
        student_dict = self.__dict__

        if attrs is not None:
            # Filter attributes based on provided list
            student_dict = {
                    key:
                    value for key,
                    value in student_dict.items() if key in attrs
                    }

        return student_dict

    def reload_from_json(self, json):
        """
        reload from json
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
