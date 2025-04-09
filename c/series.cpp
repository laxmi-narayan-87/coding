#include <stdio.h>

int main() {
    int n, i = 1;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    while (i >0) {
        printf("%d ", i);
        i--;
    }
   




 
    int a;
    scanf("%d",&a);
    int rev=0;
    int sum=0;
    while(a!=0){
        int r=a%10;
        sum=sum+r;
        rev= rev*10+r;
        a=a/10;
    }
    printf("%d",sum);
    printf("%d",rev);
    return 0;

}
