from cs50 import get_int

x = get_int("x = ")
y = get_int("y = ")

if x < y:
    print(f"x({x}) is less than y({y})")
elif y < x:
    print(f"y({y}) is less than x({x})")
else:
    print(f"x({x}) is equal to y({y})")