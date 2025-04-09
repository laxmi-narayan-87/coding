#include<stdio.h>
int swap(int *x ,int *y)
{*x=*x+*y;
*y=*x-*y;
*x=*x-*y;
}

int main()
{int a, b;
scanf("%d %d",&a , &b);
swap(&a,&b);
printf("after swap: a=%d, b=%d", a,b);

}
