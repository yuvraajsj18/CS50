#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // if (argc != 2)
    // {
    //     printf("Usage: ./bleep.c dictionary");
    //     return 1;
    // }   

    FILE *f = fopen("D:/CS50/week6/psets6/bleep/banned.txt", "r");
    if (f == NULL)
    {
        printf("File can not be opened\n");
        return 2;
    }

    char buffer[555];
    char *bannedWords[8];
    for(int t = 0; t < 8; t++)
    {
        bannedWords[t] = malloc(50);
    }
    int i = 0;
    while(fgets(buffer, 50, f))
    {
        strcpy(bannedWords[i], buffer);
        i++;
    }

    for(int s = 0; s <= i; s++)
        printf("%s", bannedWords[s]);
    
    fclose(f);

    return 0;
}