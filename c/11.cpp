#include <stdio.h>
void fun(int n)
{if (n>0){
fun(--n);
printf("%d\n",n);
fun(--n);
}
}

int main ()
{fun(3);
}
