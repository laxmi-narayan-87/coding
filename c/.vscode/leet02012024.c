#include <stdio.h>
int divide(int dividend, int divisor) {
return (dividend/divisor);     
}
int main ()
{int div, divisor;
scanf("%d%d",&div,&divisor);
printf("%d",divide(div,divisor));
}