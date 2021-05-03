#!/usr/bin/env python3
def full_name(first, last):
    if not isinstance(first, str) or not isinstance(last, str):
        raise TypeError("Both first and last names must be strings")
    if not first or not last:
        raise ValueError("Both first and last names must be non-empty")
    return f"{first} {last}"
