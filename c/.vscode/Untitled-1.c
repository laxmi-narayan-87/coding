#include <stdio.h>

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


void bubbledecsort(int arr[], int n)
{
for (int i=0; i<n-1;i++)
{
    for (int j=0; j<n-1-i;j++)
    {
	if (arr[j]<arr[j+1])
    {
	int b=arr[j+1];
	arr[j+1]=arr[j];
	arr[j]=b;
    
    }
	}
}
}



void selectionsort(int arr[], int n)
{
for (int i=0; i<n-1;i++)
{	int min=arr[i];
    int index=i;
  for (int j=i+1; j<n-1;j++)
	{if (min<arr[i]){
	min=arr[i];
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
    bubblesort(arr,n);
    printf("selection sort\n");
    selectionsort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    printf("sorted array ascending ");
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    printf("\ndesc\n");
    bubbledecsort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    
    
}


