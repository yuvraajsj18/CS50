#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str = malloc(sizeof(char) * 10);
    // str = NULL;
    printf("str = ");
    scanf("%s", str);
    if(str == NULL)
    {
        printf("Error\n");
    }
    printf("str = %s\n", str);
    return 0;
}