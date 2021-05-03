#!/usr/bin/env python3
def average(values):
    if not isinstance(values, list):
        raise TypeError("The average function only accepts non-empty lists of floats.")
    if not values:
        raise ValueError("Empty lists are not supported")
    accumulator = 0.
    for item in values:
        if not isinstance(item, float):
            raise TypeError("All values in the provided list must be float types")
        accumulator += item
    return accumulator / float(len(values))
