#include<stdio.h>
#include <math.h>
int reverse(int num) {
    int digit = (int) log10(num);
    if (num == 0)
        return 0;
    return ((num%10 * pow(10, digit)) + reverse(num/10));
}
bool isPalindrome(int x) {
int y=reverse(x);
if (y==x)
printf("true");
else 
printf("false");
}
int main()
{int x;
scanf("%d",&x);
printf("%c",isPalindrome(x));
}
