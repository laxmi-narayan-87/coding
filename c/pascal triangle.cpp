#include <stdio.h>
int factorial(int n)
{
    int f = 1; 
    for (int i = 1; i <= n; i++) 
    {
        f = f * i; 
    }
    return f; 
}
int pascal(int n, int r)
{
    return factorial(n) / (factorial(r) * factorial(n - r)); 
}
void print_pascal(int N)
{
    for (int n = 0; n < N; n++) 
    {
        for (int s = 0; s < N - n - 1; s++) 
        {
            printf(" "); 
        }
        for (int r = 0; r <= n; r++) 
        {
            printf("%d ", pascal(n, r)); 
        }
        printf("\n");
    }
}
int main()
{
    int N;
    printf("Enter the number of rows: "); 
    scanf("%d", &N);
    print_pascal(N); 
    return 0; 
}

