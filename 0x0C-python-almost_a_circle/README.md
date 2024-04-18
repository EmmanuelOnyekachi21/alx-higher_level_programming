# Project: 0x0C. Python - Almost a Circle

## Description

This project, "Almost a Circle", is part of the curriculum for 0x0C. Python, focusing on object-oriented programming concepts in Python. The project revolves around implementing classes and inheritance to create structures resembling geometric shapes, with a primary focus on circles and rectangles.

## Overview

The objective of this project is to create a class hierarchy for geometric shapes.
This hierarchy includes a base class called `Base`, which serves as the foundation for the other classes: `Rectangle` and `Square`, which are derived from `Base`, and `Circle`, which is derived from a custom class `Rectangle`.

## Project Structure

The project includes the following files:

- `models/`: This directory contains the Python files defining the classes for geometric shapes:
  - `base.py`: Defines the `Base` class, which serves as the base class for all geometric shapes.
  - `rectangle.py`: Defines the `Rectangle` class, which represents a rectangle shape.
  - `square.py`: Defines the `Square` class, which represents a square shape.
  - `circle.py`: Defines the `Circle` class, which represents a circle shape.

- `tests/`: This directory contains the unit tests for the project.

## Usage

To use the classes defined in this project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the directory containing the project files.
3. You can import the required classes into your Python scripts or interactive sessions using the following syntax:

```python
from models.rectangle import Rectangle
from models.square import Square
from models.circle import Circle
```
4. Once imported, you can create instances of the classes and utilize their methods to perform various operations on geometric shapes.

## Running Tests

To run the unit tests for this project, execute the following command in your terminal:

```bash
$ python -m unittest discover tests
```

This command will automatically discover and run all the test defined in the `test` directoory.

## Contributors
This project was developed by [Emmanuel Onyekachi] with guidance from [ALX Holberton School](https://www.alxafrica.com/)

## Acknowledgement
Special thanks to [ALX Holberton School] (https://www.alxafrica.com/)for their contributions and support during the development of this project.
