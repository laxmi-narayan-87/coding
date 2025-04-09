#include <stdio.h>
#include <math.h>

int check_smart(int n) {
    int root = sqrt(n);
    if (root * root == n)
        return 1;
    else
        retu  rn 0;
}

int main() {
    int t, n;
    scanf("%d", &t);
    scanf("%d", &n);
    for (int i = 0; i < t; i++) {
      
        if (check_smart(n))
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

