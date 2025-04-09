#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void bubblesort(int arr[], int n)
{
    int swap=0;
for (int i=0; i<n-1;i++)
{
    for (int j=0; j<n-1-i;j++)
    {
    if (arr[j]>arr[j+1])
    {
    int b=arr[j+1];
    arr[j+1]=arr[j];
    arr[j]=b;
    swap++;
    
    
    }
    }
}
}





void string_rev(char str[])
{
int n=string_len(char str[]);
int i,j;
i=0;
j=n-1;
while(i<j)
{
swap str[i] and str[j];
i++;
j--;
}
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    scanf("%d",&n);
    int char arr[n];
    gets(arr[]);
 
    //
     string_rev(char arr[n]);
    
    
    //
    puts(char arr[n]);
   
    return 0;
}








