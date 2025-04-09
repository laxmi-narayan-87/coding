#include<stdio.h>

int fact(int n)
{if (n==0)
return 1;
else
return n*fact(n-1);
}

int main()
{int N ;
scanf("%d",&N);
printf("%d\n",fact(N));
for (int i =1;i<=N;i++)
printf("%d\n",fact(i));


}
