#include <stdio.h>
#include<string.h>
int main()
{char firstname[10] , middlename[10], lastname[10];
int n,y,a,b;
gets(firstname);
gets(middlename);
gets(lastname);
char fullname[30], newname[30],neww[30];
strcpy(fullname,firstname);
strcat(fullname, " ");
puts(fullname);
strcat(fullname, " ");
strcat(fullname,middlename);
puts(fullname);
strcat(fullname, " ");
strcat(fullname,lastname);
puts(fullname);
printf("\n");
strcpy(newname,fullname);
n=strcmp(fullname,newname);
strrev(fullname);
puts(fullname);
y=strcmp(fullname,newname);
printf("%d\n",n);
printf("%d",y);
a=strcmp(firstname,middlename);
printf(" value of a :%d\n",n);
if(a==0){
printf("\nstring is in order");
printf("%s %s",firstname,middlename);
}
else{
printf("string is not in order\n");
printf("%s %s",middlename ,firstname);
}

//for palindrome string

printf("palindrome\n");
strcat(fullname,newname);
puts(fullname);
strcpy(neww,fullname);
strrev(neww);
b=strcmp(neww,fullname);

printf("\n palindrome is or not%d",b);
if(b==0)
	printf("string is palindrome");
else
printf("string is not palindrome");


}






