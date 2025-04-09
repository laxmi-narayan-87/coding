#include<stdio.h>
#include<math.h>
int main()
{
	int a[5]={10,20,30,40,50};
	int *p;
	p=a;
	printf("\n using p:");
	printf("%d ",*p);
	printf("%d ",*(p+1));
	printf("%d ",*(p+2));
	printf("%d ",*(p+3));
	printf("%d ",*(p+4));
	
	printf("\n using a:");
	printf("%d ",*a);
	printf("%d ",*(a+1));
	printf("%d ",*(a+2));
	printf("%d ",*(a+3));
	printf("%d ",*(a+4));
	
	
	
	printf("\n using different way:");
	printf("%d ",a[0]);
	printf("%d ",a[1]);
	printf("%d ",a[2]);
	printf("%d ",a[3]);
	printf("%d ",a[4]);
	
	
	printf("\n using different way:");
	printf("%d ",p[0]);
	printf("%d ",p[1]);
	printf("%d ",p[2]);
	printf("%d ",p[3]);
	printf("%d ",p[4]);
	
	
	
	p=(int*)malloc(5*sizeof(int));
	printf("\nenter the five number:");
	for (int i=0;i<5;i++)
	scanf("%d",(p+i));
	
	printf("\n your array");
	for(int i=0;i<5;i++)
	printf("%d",*(p+i));	
	
	}
