#include <stdio.h>
int main()
{int i,n,key;
scanf("%d",&n);
int arr[n];
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
scanf("%d",&key);
for(i=0;i<n;i++)
{if (key==arr[i])
{printf("%d",i);
break;
}}
if (i==n)
{printf("Key does not exist");
}
}
