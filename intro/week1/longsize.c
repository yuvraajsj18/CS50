#include <stdio.h>
#include <conio.h>

int main(void)
{

    int sizeLong = sizeof(long);
    int sizeLongLong = sizeof(long long);

    printf("size of Long = %i\nsize of Long Long = %i\n", sizeLong, sizeLongLong);

    getch();
    return 0;
}