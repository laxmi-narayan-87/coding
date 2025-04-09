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

//for 2nd matrix
printf("\nfor matrix b :\n");
for(m=0;m<3;m++)
{for ( n=0; n<3;n++)
scanf("%d",&b[m][n]);
}
printf("\nmatrix b:\n");
for(m=0;m<3;m++)
{for ( n=0; n<3;n++)
printf("%d",b[m][n]);
printf("\n");

}

printf("\nmatrix c \n");
for(x=0;x<3;x++)
{for ( y=0; y<3;y++)
c[x][y]= a[i][j]+b[i][j];
printf("%d",c[x][y]);
printf("\n");
}



for(x=0;x<3;x++)
{for ( y=0; y<3;y++)

c[x][y]=a[i][j] +b[m][n];
printf("%d",c[x][y]);
printf("\n");
}
}









