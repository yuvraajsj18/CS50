from cs50 import get_int

def main():
    numbers = [] # pythonic way of making arrays, called as a list. more flexible than array similar to linked list.
    
    while True:
        number = get_int("number: ")

        # check for EOF
        if not number:
            break
        
        # append to list
        if number not in numbers:
            numbers.append(number)
        
    # print list - numbers
    for number in numbers:
        print(number)
    
    # printing element through random access -
    print(numbers[2])

if __name__ == "__main__":
    main()
