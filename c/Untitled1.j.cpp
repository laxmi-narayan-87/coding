// C program for the above approach
#include <stdio.h>
#include <stdlib.h>

int findSQRT(int number)
{
	int start = 0, end = number;
	int mid;
	int ans;
while (start <= end) {
mid = (start + end) / 2;
if (mid * mid == number) {
			ans = mid;
			break;
		}
if (mid * mid < number) {
ans=start;
start = mid + 1;
		}
else {
			end = mid - 1;
		}
	}
	
	
	return ans;
}

// Driver Code
int main()
{

	// Given number
	int N = 2;

	// Function call
	printf("%d ", findSQRT(N));
	return 0;
}

