#include <stdio.h>
int totalMoney(int n) {
   int x=1;
    int sum = 0;
    for(int i = 1,k=1; i <= n ; i+=7,k++)
    {
        for(int j = k ; j <= 6+k;j++){
            if(x > n){
                break;
            }
            sum = sum + j;
            x++;
        }
    }
    return sum;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d ",  totalMoney(n));
    return 0;
}



