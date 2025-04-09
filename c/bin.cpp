#include<stdio.h>

void bubblesort(int arr[], int n)
{int swap=0;
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

int main()
{
    int n ,swap=0;
    scanf("%d",&n);
    int arr[n];
    for (int m=0;m<n;m++)
    scanf("%d",&arr[m]);
    printf("bubble sort");
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
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    printf("\n%d",swap);
}
