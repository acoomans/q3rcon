#!/usr/bin/python

import os
import sys


parent_dir_components = os.path.split(os.path.dirname(os.path.realpath(__file__)))
if parent_dir_components[-1] == 'scripts':
    sys.path.append(parent_dir_components[0])

from project import MyClass


def main():
    c = MyClass()
    print(c.message)


if __name__ == "__main__":
    main()