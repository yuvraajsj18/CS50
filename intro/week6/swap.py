from cs50 import get_int

x = get_int("x = ")
y = get_int("y = ")

print(f"Before Swap: x = {x} & y = {y}")

x, y = y, x

print(f"After Swap: x = {x} & y = {y}")

