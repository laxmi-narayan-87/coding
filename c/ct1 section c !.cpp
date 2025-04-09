#include<stdio.h>

int factorial(int n)
{
int fact=1;
for (int i=1;i=n;i++)
{fact=fact*i;
}
return n;
}

int sumofdigits(int a)
{
	int sum=0,d,n;
	d=n%10;
	sum=sum+d;
	n=d;
	return sum;
	
}

int multiplicationtable(int b)
{
int c;
for (int i=1;i=10; i++ )
{c=b*i;
return c;
}
}


int even_odd(int x)
{
	if (x%2==0)
	return 1;
	else
	return 0;
}



int main()
{int n,N;

 printf("1. factorial");
 printf("2. sum of digit");
 printf("3. multiplication table");
 printf("4. even odd");
 
printf(" enter the choice");
scanf("%d",&n);
printf(" enter the number");
scanf("%d",N);
switch(n)
{

case 1:printf(factorial(N));
break;
case 2:printf(sumofdigits(N));
break;
case 3:printf(multiplicationtable(N));
break;
case 4:printf(even_odd(N));
break;
default: printf("invalid choice");
 }
 return 0;
}


