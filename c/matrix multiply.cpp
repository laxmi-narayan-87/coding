#include <stdio.h>
int main()
{int m1,m2,n1,n2;
printf("enter size of first matrix:");
scanf("%d %d",&m1,&n1);
printf("enter size of second matrix:");
scanf("%d %d",&m2,&n2);
int a[m1][n1] , b[m2][n2], c[m1][n2];
//matrix a
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

//matrix b
int m,n;
for(m=0;m<m2;m++)
{for ( n=0; n<n2;n++)
scanf("%d",&b[m][n]);
}

for(m=0;m<m2;m++)
{for ( n=0; n<n2;n++)
printf("%d",b[m][n]);
printf("\n");}

// matrix c
if (n1==m2)
{
}
}
