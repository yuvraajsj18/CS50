# write a program to check the validity of a card number using luhn's algorithm

from cs50 import get_int, get_string

def main():
    # getting the card number as string to easily convert it into a list
    cardNum = get_string("Number: ")

    # list to contain digits of card number
    digits = []

    for n in cardNum:
        digits.append(int(n))

    # for n in num_int:    # testing
    #     print(n)    

    if digits[0] == 3 and (digits[1] == 4 or digits[1] == 7):
        brand = "Amex"
    elif digits[0] == 5 and (digits[1] >= 1 and digits[1] <= 5):
        brand = "Mastercard"
    elif digits[0] == 4:
        brand = "Visa"
    else:
        print("INVALID")
        exit(1)
    
    size = len(digits)
    if not size == 13 and size != 15 and not size == 16:
        print("INVALID")
        return 2
    check = checkSum(digits, size)
    if check == 1:
        print(brand)
    elif check == 0:
        print("INVALID")
    else:
        print("ERROR") 

def checkSum(digits, size):
    sumP = 0
    sumD = 0
    for i in range(size - 2, -1, -2):   # stop value should not be 0 because loop will run only till a step before stop so use -1
        product = digits[i] * 2
        while product > 0:
            digit = product % 10
            sumP += digit
            product //= 10      # using single / will not work in python as it will convert the result to float
        # sumP += product
    
    for j in range(size - 1, -1, -2):   # stop value should not be 0 because loop will run only till a step before stop so use -1
        sumD += digits[j]

    total = sumP + sumD

    if total % 10 == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
