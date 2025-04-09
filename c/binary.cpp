#include<stdio.h>
int main()
{int i,key,size;
scanf("%d",&size);
int arr[size];
for(i=0;i<size;i++)
scanf("%d",&arr[i]);
printf("key ");
scanf("%d",&key);
int start=0, end=size-1;
while(start<=end){

if (key==arr[(start+end)/2]){

printf("key is found");
break;}
else {if (key>arr[(start+end)/2])
start=((start+end)/2)+1;
else
end=((start+end)/2)-1;
}
}
}
