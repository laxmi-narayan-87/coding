#include <stdio.h>
int main()
{
    char x;
    scanf("%c", &x);
    if ((x >= 'a' && x <= 'z') || (x >= 'A' && x <= 'Z')) // check if x is an alphabet
    {
        switch(x) 
		{
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                printf("VOWEL\n" );
                break;
            default:
                printf("CONSONANT\n" );
        }
    }
    else if (x >= '0' && x <= '9') 
    {
        printf("DIGIT\n");
    }
    else 
    {
        printf("SPECIAL SYMBOL\n");
    }
    return 0;
}

