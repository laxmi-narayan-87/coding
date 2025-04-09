#include<stdio.h>
int main()
{
int x=10;
int *p;
int y=298;
p=&x;
printf("address of x=%u p=%u",&x,&*p);
printf("\nvalue of x=%d, x=%d",x,p);
*p=*p+10;
printf("\nvalue of x=%d",x);
p=&y;
printf("\n %d",*p);
printf("\n size of p:%d",sizeof(p));
printf("\n size of x:%d",sizeof(x));

char *ptr,ch='r';
ptr=&ch;
printf("\n address of  ch=%u     value of ch  =%c",ptr,*ptr);
}


