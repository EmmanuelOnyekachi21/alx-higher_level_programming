#!/usr/bin/python3
import hidden_4     # Import the compiled module

if __name__ == "__main__":
    module_names = dir(hidden_4)    # Get all names defined in the compiled module

    # Print names that do not start with '__'
    for name in sorted(module_names):
        if not name.startswith('__'):
            print(name)
