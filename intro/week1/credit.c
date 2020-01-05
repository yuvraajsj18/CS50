#include <stdio.h>
#include <conio.h>
#include <string.h>

void genArray(long long n, int arr[]);
int count(long long n);
int checkSum(int *arr, int size);

int main(void)
{
    printf("sizeof(long) = %lu\n", sizeof(long));
    long long int num;   // = get_long("Number: ");
    printf("Number: ");
    scanf("%lli", &num);
    int arr[20];                                // Array to store each digit of the number
    genArray(num, &arr[0]);
    int size = count(num);                      // Size of the array formed
    char *brand;
   
    if (arr[0] == 3 && (arr[1] == 4 || arr[1] == 7))
        strcpy(brand, "Amex");
    else if (arr[0] == 5 && ( arr[1] >= 1 && arr[1] <=5 ))
        strcpy(brand, "Mastercard");
    else if (arr[0] == 4)
        strcpy(brand, "Visa");
    else
        {
            printf("INVALID\n");
            return 0;
        }
    if (size != 13 && size != 15 && size != 16)
    {
        printf("INVALID\n");                  // Checking the size of card number if not correspond to any                                                 brand then program will terminate instantly
        return 0;
    }
    int check = checkSum(&arr[0], size);
    if (check == 1)
        printf("%s\n", brand);
    else if (check == 0)
        printf("INVALID\n");
    else
        printf("ERROR\n");

    getch();    
    return 0;
    
}

void genArray(long long n, int *arr)        // Gen Array from card num for easier handling
{
    int i = count(n) - 1;
    for ( ; i >= 0; i--)
    {
        arr[i] = n % 10;
        n /= 10;
    }
}

int count(long long n)                    // count the num of digit in card num so
{                                    // we can easily set up the array in genArray       
    int counter = 0;
    while (n != 0)
    {
        n /= 10;
        counter++;
    }
    return counter;
}

int checkSum(int *arr, int size)
{
  //  printf("size = %i\n", size);
    
    int sumP = 0;
    int sumD = 0;
    for (int i = size - 2; i >= 0; i-=2)            // start with second last digit and operate on
    {                                               // every other digit
        int product = arr[i] * 2;                    // multiply each digit by 2
        while (product > 0)
        {                                        // if the product is greater than 10 
            int digit = product % 10;            // then adding its individual digit to sumP
            sumP += digit;
            product = product / 10;
        }
        sumP += product;             // If product is single digit num then directly adding to sumP
    }
    
//    printf("sumP = %i\n", sumP);
        
    for (int j = size - 1; j >= 0; j -= 2)  // Starting by last digit
        sumD += arr[j];            // Adding every other digit

//    printf("sumD = %i\n", sumD);
    
    int total = sumP + sumD;
    
//    printf("total = %i", total);
    
    if (total % 10 == 0)
        return 1;                    // The num is valid
    else
        return 0;                // The Number is Invalid
}    

//5471151101714954
