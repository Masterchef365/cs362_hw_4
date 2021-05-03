#!/usr/bin/env python3
def cube(width, length, height):
    if not isinstance(width, float) or not isinstance(length, float) or not isinstance(height, float):
        raise TypeError("Width, length, and height must be float types")
    if width < 0 or length < 0 or height < 0:
        raise ValueError("Width, length, and height must be positive")
    return width * length * height
