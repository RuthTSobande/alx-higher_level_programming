#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)

if __name__ == "__main__":
    for f in names:
        if '__' not in f:
            print(f)
