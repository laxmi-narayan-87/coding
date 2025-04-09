#include<stdio.h>
int main()
{
	float p;
	scanf("%f",&p);
	int q;
	q=int(p);
	switch (q/10)
	{
	
		case 2:
		case 1:
		case 0: printf("grade f");
		break;
	
		case 3:printf("grade D");
		break;
		case 4:
		case 5:printf("grade C");
		break;
		case 6:
		case 7: printf("grade B ");
		break;
		case 8:
		case 9:
		case 10: printf("grade A");
		break;
		
		
		}	
	
	
}
