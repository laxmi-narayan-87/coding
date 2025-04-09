#include <stdio.h>

int main()
{
    int num1, num2; 
    char op;
    int result;

   
    scanf("%d %d", &num1, &num2);
   
    scanf(" %c", &op);

    switch (op) 
    {
        case '+': 
            result = num1 + num2;
            break; 
        case '-': 
            if (num1 < num2) 
            {
                result = num2 - num1; 
            }
            else 
            {
                result = num1 - num2; 
            }
            break;
        case '*': 
            result = num1 * num2;
            break; 
        case '/': 
            result = num1 / num2;
            break; 
       
            return 0; 
    }

    printf("%d\n", result); 
    return 0;
}

