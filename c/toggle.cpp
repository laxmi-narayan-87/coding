#include<stdio.h>
#include<math.h>

int main()
{
	int n,b,c,d;
	scanf("%d",&n);
	c=n>>1;
	b=(~n);
	d=(~c);
	printf("%d\n",b);
	printf("%d\n",d);
	
}
