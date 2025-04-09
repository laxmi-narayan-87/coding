#include <stdio.h>
int main(){
int b[3][3];
int a[3][3];
int c[3][3];
int i,j,m,n,x,y;
int sum=0;
for(i=0;i<3;i++)
{for ( j=0; j<3;j++)
scanf("%d",&a[i][j]);
}
printf("matrix A :\n");
for(i=0;i<3;i++)
{for ( j=0; j<3;j++)
printf("%d",a[i][j]);
printf("\n");}

for(i=0;i<3;i++)
{for (j=0; j<3;j++)
sum = sum+a[i][j];
printf("\nsum=%d",sum);
sum=0;}
.
