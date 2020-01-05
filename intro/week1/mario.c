// program to print a pyramid for mario (Pset1)
// Yuvraj S Jadon
#include </media/yuvrajsj18/New Volume/cs50/cs50.c>
#include <stdio.h>

int main(void)
{
    int height;
    // Take input as long as it is not in range 1-8
    do
    {
        height = get_int("Height: ");
    }
    while(height < 1 || height > 8);
       
    for (int i = 1; i <= height; i++)            // i measures height in each run of this loop
    {
        for(int s = 0; s < height - i; s++)    // s represents the number of spaces before first '#'
             printf(" ");
        for(int k = 0; k < 2; k++)                // this loop with k gives the shape of pyramid
        {
            for(int n = 0; n < i; n++)          // n represents the number of '#' each line will have
                printf("#");
            if(k < 1)
                printf("  ");
        }
        printf("\n");    
    }
}
