#!/usr/bin/python3
import hidden_4     # Import the compiled module

if __name__ == "__main__":
    for value in dir(hidden_4):
        if value[:2] == "__":
            continue
        print(value)
