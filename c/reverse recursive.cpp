#include <stdio.h>
#include<math.h>

int reverse1(int a )
{if (a== 0)
    return 0;
else
{
int r = a%10;
int d = log10(a) +1;
return(r*pow(10,d)+reverse1(a/10));
}
}

int fib(int n)
{if (n==1)
return 0;
if (n==2)
return 1;
else
return fib (n-1)+fib(n-2);
}
















int main()
{
printf("reverse1");
int num1, rev1;
scanf("%d", &num1);
rev1=reverse1(num1);
printf(" %d , %d", num1,rev1);


printf(" \n\n\n\n\n\n");

int n;
printf("fibonacci");
scanf("%d",&n);
printf("%d\n",fib (n));
for (int i=1;i<=n;i++)
printf("%d",fib (i));
return 0;
}
