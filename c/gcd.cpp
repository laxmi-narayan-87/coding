#include <stdio.h>

int main() {
    int num1, num2, i, gcd1, gcd2, gcd3, gcd4, gcd5;
    printf("Enter two positive integers: ");
    scanf("%d %d", &num1, &num2);
    for (i = 1; i <= num1 && i <= num2; ++i) {
        if (num1 % i == 0 && num2 % i == 0) {
            gcd1 = i;
        }
    }
    while (num1 != 0 && num2 != 0) {
        if (num1 > num2) {
            num1 %= num2;
        } else {
            num2 %= num1;
        }
    }
    gcd2 = num1 == 0 ? num2 : num1;
    do {
        if (num1 > num2) {
            num1 -= num2;
        } else {
            num2 -= num1;
        }
    } while (num1 != num2);
    gcd3 = num1;
    int marks[num1];
    for (i = 0; i < num1; i++) {
        scanf("%d", &marks[i]);
    }
    for (i = 1; i <= num1 && i <= num2; ++i) {
        if (num1 % i == 0 && num2 % i == 0) {
            gcd4 = i;
        }
    }
    while (num1 != 0 && num2 != 0) {
        if (num1 > num2) {
            num1 %= num2;
        } else {
            num2 %= num1;
        }
    }
    gcd5 = num1 == 0 ? num2 : num1;
    printf("GCD of %d and %d using for loop is %d.\n", num1, num2, gcd1);
    printf("GCD of %d and %d using while loop is %d.\n", num1, num2, gcd2);
    printf("GCD of %d and %d using do-while loop is %d.\n", num1, num2, gcd3);
    printf("GCD of %d and %d using for loop and Euclidean algorithm is %d.\n", num1, num2, gcd4);
    printf("GCD of %d and %d using while loop and Euclidean algorithm is %d.\n", num1, num2, gcd5);
    return 0;
}

