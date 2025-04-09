#include<stdio.h>

typedef struct{
	char name[20];
	int id;
	char branch[30];
	int contactno;	
}student;

int main()
{
FILE*fp;
fp=fopen("stupoint.txt","w");
student s;
for (int i=1; i<5;i++)
{printf("enter record of students");
fflush(stdin);
gets(s.name);
scanf("%d",&s.id);
gets(s.branch);
scanf("%d",&s.contactno);
fflush(s.name);
fprintf(fp, "%s %d %s %d",s.name,s.id,s.branch,s.contactno);
}
fclose(fp);

fp=fopen("stupoint.txt","w");
for (int i=1; i<5;i++)
{fscanf(fp, "%s %d %s %d",&s.name,&s.id,&s.branch,&s.contactno);
printf(fp,"%s %d %s %d",s.name,s.id,s.branch,s.contactno);

}
 } 
