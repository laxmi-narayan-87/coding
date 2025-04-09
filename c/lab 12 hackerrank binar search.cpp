#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
     int size,num,i,count1=0 ;
    scanf("%d",&size);
    int arr[size];
    for(i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
        scanf("%d",&num);

    for(i=0;i<size-1;i++){
    if(arr[i+1]>arr[i]){
        count1++;
    }
    else {
        printf("Binary search could not be implemented");
        break;
    }
    }
    if(count1==size-1){
        int start=0,end=size-1,count2=0;
        while(start<=end){
        int mid=(start+end)/2;
        if(num==arr[mid]){
            printf("%d",mid);
            count2=1;
            break;
        }
        else if(num>arr[mid]) start=mid+1;
        else end=mid-1;
        }
        if(count2==0){
            printf("Key does not exist");
        }
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;}
