#include<stdio.h>
int main()
{
FILE*fp;
fp=fopen("newpointer.txt","w");
char ch;
ch=getchar();
while(ch!=EOF)
{putc(ch,fp);
ch=getchar();
}
fclose(fp);

fp=fopen("newpointer.txt","r");

ch=getc(fp);
while(ch!=EOF)
{putc(ch,fp);
ch=getc(fp);
}
fclose(fp);
}
