#include <stdio.h>
int main()
{
int abc[10], i,max,min;
printf("enter element of array");
for (i=0; i<10; i++)
scanf("%d",&abc[i]);
for (i=0; i<10; i++)
printf("%d\n",abc[i]);

max=abc[0];
for (i=0; i<10; i++)
{if (max<abc[i])
max=abc[i];
}
printf("max=%d",max);

min=abc[0];
for (i=0; i<10; i++)
{if (min>abc[i])
min=abc[i];
}
printf("min=%d\n",min);

int search;
scanf("%d",&search);

for (i=0; i<10; i++)
{if (search==abc[i])
printf("yes"); 
  break; 
 } 
printf("function\n new search");

printf("yes",sear);

}
int sear(int abc[]){
	int new;
scanf("%d"&new);
for (int j=0; j<10; j++)
{if (new==abc[z])
return 1; 
}}













}
