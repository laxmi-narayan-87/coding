#include <stdio.h>
#include <math.h>
#include<limits.h>
int divide(int dividend, int divisor) {
  if (divisor == 0) {
    printf("Error: division by zero\n");
    return 0;
  }
  if (dividend == INT_MIN || divisor == INT_MIN) {
    if (dividend == divisor) {
      return 1; 
    }
    if (divisor == -1) {
      printf("Error: overflow\n");
      return INT_MAX; 
    }
    if (dividend == INT_MIN) {
      dividend++;
    } else {
      divisor++;
    }
  }
  int result = dividend / divisor;
  if (result > INT_MAX) {
    printf("Error: overflow\n");
    return INT_MAX; 
  }
  return result;
}

int main ()
{int div, divisor;
scanf("%d%d",&div,&divisor);
printf("%d",divide(div,divisor));
}
