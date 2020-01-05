# write a program using python to print a pyramid similar to that of mario with #s

#   Height: 4
#      #  #
#     ##  ##
#    ###  ###
#   ####  ####

from cs50 import get_int

def main():
    #take input for height
    while True:
        height = get_int("Height: ")
        if height > 0 and height <= 8:
            break

    for storey in range(1, height + 1):     # storey stores the current line in pyramid with top being 1 and last being height
        for _ in range(height - storey):    # this will put spaces as required before starting to print #s
            print(" ", end = "")
        for k in range(2):      # to repeat printing #s with a space in between
            for _ in range(storey):     # will print spaces required number of times
                print("#", end="")
            if k < 1:
                print(" ", end="")
        print()        

if __name__ == "__main__":
    main()