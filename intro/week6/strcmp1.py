from cs50 import get_string

s = get_string("s: ").lower()
y = get_string("y: ").lower()

if s == y:
    print(f"Given Strings are equal")
else:
    print(f"Given String Are Not Equal")