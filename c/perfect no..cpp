#include <stdio.h>

// Function to get sum of divisors
int getSum(int n) {
    int i, sum = 1;
    
    for ( i = 2; i * i <= n; i++) 
	{
        if (n % i == 0) {
            if (i * i != n)
                sum = sum + i + n / i;
            else
                sum = sum + i;
        }
    }
    return sum;
}

// Function to check if the number is perfect
void isPerfect(int n) {
    if (getSum(n) == n)
        printf("YES\n");
    else
        printf("NO\n");
}

int main() {
    int N;
    scanf("%d", &N);
    isPerfect(N);
    return 0;
}

