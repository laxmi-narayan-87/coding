# Maximise the Sum
# Problem Statement
# You are given an array with N integers: A[1], A[2], . . . , A[N] (where N is even). You are
# allowed to permute the elements however you want. Say, after permuting the elements,
# you end up with the array A′
# [1], A′
# [2], . . . , A′
# [N]. Your goal is to maximize the following
# sum:
# |A
# ′
# [1] − A
# ′
# [2]| + |A
# ′
# [3] − A
# ′
# [4]| + · · · + |A
# ′
# [N − 1] − A
# ′
# [N]|
# Here, |x| denotes the absolute value of x.
# You have to print the maximum sum achievable.
# Input Format
#  The first line contains T, the number of test cases.
#  Each test case starts with an integer N in the first line.
#  The second line of each test case contains N space-separated integers, denoting the
# values of array A.
# Output Format
# For each test case, output the maximum sum achievable in a new line.
# Constraints
#  1 ≤ T ≤ 105
#  1 ≤ N ≤ 105
#  N is even
#  |A[i]| ≤ 109
#  Sum of N over all test cases ≤ 2 × 105

# Example Input
# 1
# 4
# 1 -3 2 -3
# Example Output
# 9
# Explanation
# The original array is {1, −3, 2, −3}.
# Suppose you permute it and get the array {2, 1, −3, −3}. Then the corresponding
# sum would be:
# |2 − 1| + |−3 − (−3)| = 1 + 0 = 1
# But suppose you permute it differently and get the array {−3, 2, 1, −3}. Then the
# corresponding sum would be:
# |−3 − 2| + |1 − (−3)| = 5 + 4 = 9
# You can check that you cannot do any better, and hence the answer is 9.


# write the most optimised code for the above problem statement. 
# note: before compiling the code one more time check the code for more than 100 hidden test cases as well.WindowsError
    

def maximise_sum(t, n, a):
    a.sort()
    s = 0
    for i in range(0, n, 2):
        s += a[i + 1] - a[i]
    return s
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(maximise_sum(t, n, a))


# Time Complexity: O(nlogn)
# Space Complexity: O(n)








write a program to find second largest in array in python 3

def second_largest(self,arr):
    if len(arr) < 2:
        return -1
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

        





Second Largest
Difficulty: EasyAccuracy: 26.72%Submissions: 805K+Points: 2
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

def getsecondlargest(arrself,arr):
    if len(arr) < 2:
        return -1
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

# Time Complexity: O(n)
# Space Complexity: O(1)

For Input: 
12 35 1 10 34 1
Your Output: 
-inf
Expected Output: 
34
Output Difference



def getsecondlargest(arrself,arr):
    if len(arr) < 2:
        return -1
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


































Count Periodic Numbers
Problem Statement
A positive integer n is said to be periodic if it satisfies the following property:
Take the binary representation of n without leading zeros. Then create an array which
contains the length of consecutive runs of equal bits in this binary representation. All the
elements of this array should be equal. If there are two unequal elements in this array,
then n is not periodic.
Examples
 Suppose n = 3. Its binary representation is 11. The array created would be {2},
which corresponds to the fact that there are two equal bits at the beginning. This
is periodic.
 Suppose n = 51. Its binary representation is 110011. The array created would
be {2, 2, 2}, which corresponds to the fact that there are two equal bits at the
beginning, then the next two are equal, and then the next two are equal. This is
also periodic.
 Suppose n = 103. Its binary representation is 1100111. The array created would
be {2, 2, 3}, which corresponds to the fact that there are two equal bits at the
beginning, then the next two are equal, and then the next three are equal. This is
not periodic because the array contains two different values (2 and 3).
You are given two integers L, R. Find the number of integers in the range [L, R] (both
inclusive) that are periodic.
Input Format
 The first line of the input contains an integer T denoting the number of test cases.
 Each test case consists of one line containing two space-separated integers L, R.
Output Format
For each test case, output a single line containing an integer corresponding to the number
of periodic numbers in the range [L, R].

Constraints
 1 ≤ T ≤ 105
 1 ≤ L, R ≤ 109
Example Input
2
3 3
1 10
Example Output
1
6
Explanation
Testcase 1: The only number between L and R is 3, which is periodic. Hence the answer
is 1.
Testcase 2: The periodic numbers between 1 and 10 are 1, 2, 3, 5, 7, 10. Since there
are six of them, the answer is 6.



code:

def generate_periodic_numbers(limit):
    periodic_numbers = set()
    for bits in range(1, 31):
        for pattern in range(1, (1 << bits)):
            num = int(bin(pattern)[2:], 2)
            while num <= limit:
                if num not in periodic_numbers:
                    periodic_numbers.add(num)
                num = (num << bits) + pattern
    return sorted(periodic_numbers)
LIMIT = 10**9
periodic_numbers = generate_periodic_numbers(LIMIT)
def solve(L, R):
    return sum(1 for num in periodic_numbers if L <= num <= R)
T = int(input())
for _ in range(T):
    L, R = map(int, input().split())
    print(solve(L, R))

# Time Complexity: O(T * log(N))
# Space Complexity: O(2^31)




































Colliding Balls Problem
Problem Statement
There are n red balls kept on the positive X axis, and m blue balls kept on the
positive Y axis. You are given the positions of the balls. For each i from 1 to n,
the i-th red ball has the coordinates (xi
, 0), where xi
is a positive integer. For
each i from 1 to m, the i-th blue ball has the coordinates (0, yi), where yi
is a
positive integer.
It is given that all xi are distinct. Also, all yi are distinct.
At time t = 0, for each i from 1 to n, the i-th red ball is thrown towards
the positive Y axis with a speed of ui (that is, with velocity vector (0, ui)).
Simultaneously (at time t = 0), for each i from 1 to m, the i-th blue ball is
thrown towards the positive X axis with a speed of vi (that is, with velocity
vector (vi
, 0)).
Two balls are said to collide if they are at the same position at the same
time. When two balls collide, they disappear and no longer collide with other
balls.
Your task is to find the total number of collisions that occur between the
balls.
Input
 The first line contains n and m, the number of red balls and the number
of blue balls, respectively.
 The next n lines each contain two space-separated integers xi and ui
,
representing the position and speed of the i-th red ball, respectively.
 The next m lines each contain two space-separated integers yi and vi
,
representing the position and speed of the i-th blue ball, respectively.
Output
Print the total number of collisions.
1
Constraints
 1 ≤ n, m ≤ 105
 1 ≤ xi
, ui
, yi
, vi ≤ 109
 For all 1 ≤ i < j ≤ n, xi ̸= xj
 For all 1 ≤ i < j ≤ m, yi ̸= yj
Example
Input 1
1 1
1 2
2 1
Output 1
1
Input 2
1 2
1 2
2 1
1 2
Output 2
1
Explanation
 Example Case 1: The balls collide at t = 1, at the coordinates (1, 2).
 Example Case 2: The red ball and the second blue ball collide at time
t = 0.5 at coordinates (1, 1). Note that the first blue ball would have
collided with the red ball at t = 1 (like in sample input #1), if the second
blue ball wasn’t present. However, since the red ball disappears at t = 0.5,
its collision with the first blue ball does not happen. Thus, the total
number of collisions is 1.





#full program for above problem write the optimised code for above problem also take input from the system
# and print the output as well. consider all possibilties and constraints before writing the code.

def count_collisions(n, m, red_balls, blue_balls):
    collisions = 0
    red_balls.sort(key=lambda x: x[0])
    blue_balls.sort(key=lambda x: x[1])

    i, j = 0, 0
    while i < n and j < m:
        xi, ui = red_balls[i]
        yi, vi = blue_balls[j]
        
        if xi / vi == yi / ui:
            collisions += 1
            i += 1
            j += 1
        elif xi / vi < yi / ui:
            i += 1
        else:
            j += 1

    return collisions
    #take bulk input 
n, m = map(int, input().split())
red_balls = [list(map(int, input().split())) for _ in range(n)]
blue_balls = [list(map(int, input().split())) for _ in range(m)]
print(count_collisions(n, m, red_balls, blue_balls))
