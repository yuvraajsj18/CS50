/*
    A program to implement vigenere's cipher.
    It take the keyword as an cmd line arg and plaintext from user
    and process it to print a scrambled version of plain text.
 */
#include <D:\CS50\cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(int argc, string argv[])    //int main(int argc, string argv[])
{
    //check no of arguments = 2 or not
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
   // validate argument - each character should be alphabet
   int count = 0; //to count the no of letters in keyword
    for (int i = 0; argv[1][i] != '\0'; i++)
    {
        count++;
        if(!(isalpha(argv[1][i])))
        {
            printf("Usage: ./vigenere keyword\n");
            return 2;
        }
    }
    // Input plaintext
    string text = get_string("plaintext: ");
    // Cipher's Implementation --->
    for (int i = 0, j = 0; text[i] != '\0'; i++)   // iterate over every letter of plaintext, j represents                                                         keyword's letter's postion
    {
        int key;
        if(isupper(argv[1][j]))
            key = ( (int) argv[1][j] ) % ( (int) 'A' );    //find the key as a = 0,
        else if(islower(argv[1][j]))                            //b = 1, c = 2......
            key = ( (int) argv[1][j] ) % ( (int) 'a' );     //type casting from char to int
        int shift;
        if(isupper(text[i]))
        {
            shift = text[i] + key;
            while(shift > 'Z')   // wraping from above Z
                shift = ('A' - 1) + (shift % 'Z');     // implicit casting from char to int
            text[i] = shift;

                if(j < count - 1)
                    j++;
                else
                    j = 0;
        }
        else if(islower(text[i]))
        {
            shift = text[i] + key;
            while(shift > 'z')    // wraping from above z
                shift = ('a' - 1) + (shift % 'z');     // implicit casting from char to int
            text[i] = shift;

            if(j < count - 1)
                j++;
            else
                j = 0;
        }
    }
    // printing ciphertext --->
    printf("ciphertext: %s\n", text);

    return 0;
}
