#include <stdio.h>
#include <stdlib.h>

int days_from_date(int d, int m, int y) {
  if (m <= 2) {
    y--;
    m += 10;
  }
  else {
    m -= 2;
  }

  int n = 365*y + y/4 - y/100 + y/400 + (306*m + 5)/10 + (d - 1);

  if (y > 1582 || (y == 1582 && (m > 10 || (m == 10 && d > 14)))) {
    int c = y/100 - y/400 - 2;
    n -= c;
  }

  return n;
}

int days_between_dates(int d1, int m1, int y1, int d2, int m2, int y2) {
  int n1 = days_from_date(d1, m1, y1);
  int n2 = days_from_date(d2, m2, y2);

  return abs(n2 - n1);
}

int main() {
  int d1, m1, y1, d2, m2, y2;

  printf("Enter the first date (dd/mm/yyyy): ");
  scanf("%d/%d/%d", &d1, &m1, &y1);

  printf("Enter the second date (dd/mm/yyyy): ");
  scanf("%d/%d/%d", &d2, &m2, &y2);

  int days = days_between_dates(d1, m1, y1, d2, m2, y2);

  printf("The number of days between the two dates is %d\n", days);

  return 0;
}

