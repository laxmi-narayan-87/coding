#include<stdio.h>

void maxselectionsort(int arr[], int n)
{
for (int i=n-1; i>1;i--)
{	int max=arr[i];
    int index=i;
  for (int j=0; j<n-1;j++)
	{if (max<arr[i]){
	max=arr[i];
   index=j;
    }
	}
	int b=arr[index];
	arr[index]=arr[i];
	arr[i]=b;
}}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for (int m=0;m<n;m++)
    scanf("%d",&arr[m]);
    maxselectionsort(arr,n);
    printf("selection sort\n");
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
}
