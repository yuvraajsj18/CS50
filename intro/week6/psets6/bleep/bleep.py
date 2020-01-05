from cs50 import get_string
from sys import argv


def main():

    if not len(argv) == 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    file = open("D:/CS50/week6/psets6/bleep/banned.txt", 'r')
    bannedWords = set()
    for ch in file:
        bannedWords.add(ch.strip('\n'))
    
    message = get_string("What message would you like to censor?\n")
    
    words = message.split()

    # for word in words:
    #     star = []
    #     for bannedWord in bannedWords:
    #         if bannedWord == word.lower():
    #             words.remove(word)
    #             for _ in range(len(word)):
    #                 star.append('*')
    #             starStr = "".join(star)
    #             words.append(starStr)
    for word in words:
        star = ""
        for bannedWord in bannedWords:
            if bannedWord == word.lower():
                words.remove(word)
                for ch in word:
                    star += "*"
                words.append(star)
                    

    for word in words:
        print(word, end=" ")

    file.close()

if __name__ == "__main__":
    main()
