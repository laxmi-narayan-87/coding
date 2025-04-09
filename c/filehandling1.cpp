#include<stdio.h>
int main()
{
FILE*fp1,*fp2;
fp1=fopen("newpointer.txt","r");
fp2=fopen("newpointer2.txt","w");

char ch;
ch=getc(fp1);
while(ch!=EOF)
{putc(ch,fp2);
ch=getc(fp1);
}



fclose(fp1);
fclose(fp2);

FILE*fp;
fp=fopen("newpointer2.txt","r");
while(ch!=EOF)
{printf("%c",ch)
ch=getc();
}

}
