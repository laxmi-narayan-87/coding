#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// to divide a number into sum of two prime numbers 
// 10= 3+7
//10=5+5


int count(int a)
{
    int c=0;
    for(int i=1;i<a;i++)
    {
        if(a%i==0)
        {
            c++;
        }
    }
    return c;
}
int main() 
{
    int n;
    int z=0;
    scanf("%d",&n);
    
    for(int i=1;i<=n/2;i++)
    {
        if(count(i)==1)
        {
            for(int j=1;j<=n;j++)
            {
                if(count(j)==1)
                {
                    if((i+j)==n)
                    {
                        z++;
                        printf("%d=%d+%d\n",n,i,j);
                    }
                }
            }
        }
    }
    if(z==0)
    printf("NOT POSSIBLE");
    
return 0;
}

