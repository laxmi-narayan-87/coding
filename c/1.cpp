#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


void stringinsertionsort(char arr[])
{if (strlen(arr)=='1')
return;
int i,j,key;
for (i=1;i<strlen(arr);i++)
{key=arr[i];
for (j=i-1;j>=0&& key<arr[j];j--)
arr[j+1]= arr[j];
arr[j+1]=key;
}
}



int main()
{
    int n;
    scanf("%d",&n);
    char arr[n];
	gets(arr);
    stringinsertionsort(arr);
    puts(arr);
}

