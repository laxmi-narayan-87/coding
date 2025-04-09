#include<stdio.h>
int main()
{int m,n;
scanf("%d%d",&m,&n);
int a1[m],a2[n];
int arr3[m+n];
for(int i=0;i<m;i++)
scanf("%d",a1[i]);
for(int i=0;i<n;i++)
scanf("%d",a2[i]);

int left=0,right=0,index=0;
while(left<m&&right<n)
{if(a1[left]<a2[right])
{arr3[index]=a1[left];
left++,index++;
}
else
{arr3[index]=a2[right];
right++,index++;
}
}
while(left<m)
{arr3[index]=a1[left];
left++,index++;
}
while(right<n)
{arr3[index]=a2[right];
index++,right++;
}

for(int i=0;i<(m+n);i++)
printf("%d",arr3[i]);
}
