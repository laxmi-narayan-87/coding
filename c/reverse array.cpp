#include <stdio.h>
int main()
{int i,n;
scanf("%d",&n);
int arr[n];
for(i=0;i<n;i++)
scanf("%d",&arr[i]);
for(i=0;i<n;i++)
printf("%d",arr[i]);

printf("after reverse\n");
int j=n-1;
i=0;
while(i<j)
{for(i=0;i<n;)
{
arr[i]=arr[j];
arr[j]=arr[i];
printf("%d",arr[i]);
i++;
j--;

}
}


}


