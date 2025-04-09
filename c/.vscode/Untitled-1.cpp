#include <stdio.h>
int main()
{int n;
scanf("%d",&n);
int arr[n];
for (int i=0;i<n;i++)
scanf("%d",&arr[i]);
for (int i=n;i=1;i++)
{
for (int j=i;j<n;j++)
{if (arr[i]<arr[j])
arr[i]=arr[j];
}
}
for (int i=0;i<n;i++)
printf("%d",arr[i]);
}