#include <stdio.h>
int main()
{int i,n;
scanf("%d",&n);
int arr[n];
for(i=0;i<n;i++)
scanf("%d",&arr[i]);

reverse(arr,n);
for(i=0;i<n;i++)
printf("%d",arr[i]);
}
void reverse(int a[],int n)
{int i=0, j=n-1;
while(i<j)
{swap(a[i],a[j]);
i++,j++;
return
}
}

void swap()
{int a;
int i=a[i];
a[i]=a[j];
return a[j];
}
