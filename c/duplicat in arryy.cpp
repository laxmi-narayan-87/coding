#include<stdio.h>
#include<math.h>
// decimal to binary
void dec_to_bin(int dec)
{
    int bin = 0;
    int i = 1;
    while (dec > 0) 
    {
        int rem = dec % 2; 
        dec = dec / 2; 
        bin = bin + rem * i; 
        i = i * 10; 
    }
 
}
int main()
{int n;
scanf("%d",&n);
dec_to_bin(n);
printf("%d",n);
}
