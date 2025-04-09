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

int removeDuplicates(int a[], int numsSize){

    int new_size = numsSize;
    for (int idx = 0, i = 0, j = 1; i < numsSize; idx++, j++) {
        while(j < numsSize && a[i] == a[j]) {
            j++;
            new_size--;
        }
        a[idx] = a[j-1];
        i = j;
    }
    return new_size;
}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for (int m=0;m<n;m++)
    scanf("%d",&arr[m]);
    printf("bubble sort\n");
    bubblesort(arr,n);
    for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
    for(int i=0;i<n;i++)
	{if (arr[i]==arr[i+1]){
	printf(" %d",i);
	printf(" \n%d",arr[i]);
	}
	}
	printf("\n\n");
	removeDuplicates(arr,n);
	for (int i=0; i<n;i++)
    printf(" %d",arr[i]);
	}




