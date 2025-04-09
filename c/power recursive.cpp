#include<stdio.h>
int power(int a, int b)
{
	if(b==0)
	return 1;
	else 
	return a*power(a,b-1);
	
}

int main()
{
 int m,n;
scanf("%d %d",&m,&n);
printf("%d", power(m,n));
return 0;
}
