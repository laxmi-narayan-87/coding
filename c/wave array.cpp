#include<stdio.h>

void bubblesort(int arr[], int n)
{
for (int i=0; i<n-1;i++)
{
    for (int j=0; j<n-1-i;j++)
    {
	if (arr[j]>arr[j+1])
    {
	int b=arr[j+1];
	arr[j+1]=arr[j];
	arr[j]=b;
    
    }
	}
}
}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for (int m=0;m<n;m++)
    scanf("%d",&arr[m]);
    bubblesort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    printf("\n wave ");
    for (int i=0; i<n;i++){
    if (i%2==0)
    {int a= arr[i];
    arr[i]=arr[i+1];
    arr[i+1]= a;
	}
	}
	for (int i=0; i<n;i++)
	printf(" %d",arr[i]);
}
