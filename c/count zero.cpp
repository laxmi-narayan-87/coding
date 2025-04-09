#include<stdio.h>
int main()
{int m1,n1;
printf("enter size of first matrix:");
scanf("%d %d",&m1,&n1);
int a[m1][n1];
int i,j;
for(i=0;i<m1;i++)
{for ( j=0; j<n1;j++)
scanf("%d",&a[i][j]);
}
printf("\nmatrix a:\n");
for(i=0;i<m1;i++)
{for ( j=0; j<n1;j++)
printf("%d",a[i][j]);
printf("\n");}


//transpose
}

