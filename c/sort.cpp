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


void insertionsort(int arr[], int n)
{if (n==1)
return;
int i,j,key;
for (i=1;i<n;i++)
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
    int arr[n];
    for (int m=0;m<n;m++)
    scanf("%d",&arr[m]);
    printf("bubble sort");
    bubblesort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    printf("insertion sort");
    insertionsort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    
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



