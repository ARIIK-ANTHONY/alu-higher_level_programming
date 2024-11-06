#!/usr/bin/python3
from base_geometry import BaseGeometry

bg = BaseGeometry()

# Test integer_validator without exceptions
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

# Test integer_validator with exceptions
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")

try:
    bg.integer_validator("height", "four")
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")

try:
    bg.integer_validator("age", (4,))
except Exception as e:
    print(f"[{e.__class__.__name__}] {e}")
