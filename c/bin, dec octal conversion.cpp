#include <stdio.h>
#include <math.h>

int bin_to_dec(int bin)
{
    int dec = 0; 
    int i = 0; 
    while (bin > 0) 
    {
        int rem = bin % 10; 
        bin = bin / 10; 
        dec = dec + rem * pow(2, i);
        i++; 
    }
    return dec;
}

int dec_to_bin(int dec)
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
    return bin; 
}

int dec_to_oct(int dec)
{
    int oct = 0; 
    int i = 1; 
    while (dec > 0) 
    {
        int rem = dec % 8; 
        dec = dec / 8; 
        oct = oct + rem * i; 
        i = i * 10;
    }
    return oct; 
}

int oct_to_dec(int oct)
{
    int dec = 0; 
    int i = 0; 
    while (oct > 0) 
    {
        int rem = oct % 10; 
        oct = oct / 10; 
        dec = dec + rem * pow(8, i); 
        i++; 
    }
    return dec; 
}

int main()
{
    int bin = 1010; 
    int dec = 15; 
    int oct = 17; 

    printf("Binary %d is equal to decimal %d\n", bin, bin_to_dec(bin)); 
    printf("Decimal %d is equal to binary %d\n", dec, dec_to_bin(dec)); 
    printf("Decimal %d is equal to octal %d\n", dec, dec_to_oct(dec)); 
    printf("Octal %d is equal to decimal %d\n", oct, oct_to_dec(oct)); 

    return 0; 
}

























