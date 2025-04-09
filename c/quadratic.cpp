#include <stdio.h>
#include <math.h>

int main()
{

    int a,b,c,d;
    double root1, root2, realPart, imaginaryPart;

    scanf("%d %d %d", &a, &b, &c);

    d = b * b - 4 * a * c;

    if (d > 0)
    {
        root1 = (-b + sqrt(d)) / (2.0 * a);
        root2 = (-b - sqrt(d)) / (2.0 * a);

        printf("REAL AND DISTINCT\n");
        printf("%.2lf %.2lf", root1, root2);
    }

    else if (d == 0)
    {
        root1 = root2 = -b / (2.0 * a);

        printf("REAL AND EQUAL\n");
        printf("%.2lf %.2lf", root1, root2);
    }

       else
    {
        realPart = -b / (2.0 * a);
        imaginaryPart = sqrt(-d) / (2.0 * a);

        printf("IMAGINARY ROOTS\n");
        printf("%.2lf+%.2lfi %.2lf-%.2lfi", realPart, imaginaryPart, realPart, imaginaryPart);
    }

    return 0;
}
