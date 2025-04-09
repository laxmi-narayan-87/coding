#include <stdio.h>
int main()
{char firstname[10] , middlename[10], lastname[10];
gets(firstname);
gets(middlename);
gets(lastname);
char fullname[30];
strcpy(fullname,firstname);
strcat(fullname, " ");
strcpy(fullname,middlename);
strcat(fullname, " ");
strcpy(fullname,lastname);
puts(fullname);
}