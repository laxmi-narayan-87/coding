#include<conio.h>
#include<stdio.h>
#include<math.h>
int main()
{int n;
scanf("%d",&n);
int arr[n];
for (int i=0;i<n;i++)
scanf("%d",arr[i]);

for (i=0;i<n;i++)
printf("%d",arr[i]);


}

void rotate(int a[],int n)
{int z,key;
scanf("%d",&z);
for (int i=0;i<z;i++)
{key=a[n-1];
for (int j=n-1;j>0;j--)
a[j]=a[j-1];
a[0]=key;
}
}




