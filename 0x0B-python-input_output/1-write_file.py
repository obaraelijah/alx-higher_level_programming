#!/usr/bin/python3
def num_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
