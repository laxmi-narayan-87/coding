#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// sum of sine series
// lab 9
int fact(int n)
{
    int i,f=1;
    for(i=1;i<=n;i++)
    {
        f=f*i;
    }
    return f;
}
int main()
{
    float sum=0,x;
    int n,i,k=1;
    scanf("%f",&x);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        sum=sum+(float)pow(x,k)/fact(k)*pow(-1,i+1);
        k=k+2;
    }
    printf("%0.6f",sum);
    return 0;
}
