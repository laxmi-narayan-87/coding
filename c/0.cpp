#include <stdio.h>

// Function prototype
int Reverse(int num);

int main()
{
    int num, rev;

    // Input number from user
    printf("Enter any number: ");
    scanf("%d", &num);

    // Call the function to reverse number
    rev = Reverse(num);

    printf("Reverse of %d = %d\n", num, rev);

    return 0;
}

// Recursive function to reverse a number
int Reverse(int num)
{
    // Base case: when the number is 0, return 0
    if (num == 0)
        return 0;
    else
        // Recursive case: reverse the remaining digits and multiply by 10
        // Then add the last digit to the result
       return (Reverse(num / 10) * 10) + (num % 10);
}

