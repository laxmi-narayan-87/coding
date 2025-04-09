#include<stdio.h>
#include<stdlib.h>
int main()
{int *p;
p=(int*)malloc(20);
for (int i=0;i<5;i++)
scanf("%d",p[i]);
for (int i=0;i<5;i++)
printf("%d",p[i]);

}
