#!/usr/bin/env python3

def cube(x):
    """Returns the cube of x"""
    return x**3
def test_cube():
    assert cube(0) == 0
    assert cube(2) == 8
    assert cube(-2) == -8