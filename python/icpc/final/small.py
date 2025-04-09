# Small Indices
# You are given two arrays 
# A
# A and 
# B
# B of size 
# N
# N.

# You need to construct an array 
# C
# C of size 
# N
# N. For 
# 1
# ≤
# i
# ≤
# N
# 1≤i≤N, you can choose 
# C
# i
# C 
# i
# ​
#   to be either 
# A
# i
# A 
# i
# ​
#   or 
# B
# i
# B 
# i
# ​
#  .

# A small index is defined as an index 
# i
# i that satisfies both of the following conditions:

# i
# ≥
# 3
# i≥3;
# There exist indices 
# j
# j and 
# k
# k such that 
# 1
# ≤
# j
# <
# k
# <
# i
# 1≤j<k<i and 
# C
# i
# ≤
# C
# j
# +
# C
# k
# C 
# i
# ​
#  ≤C 
# j
# ​
#  +C 
# k
# ​
#  .
# Find the maximum number of small indices you can get.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of three lines of input.
# The first line of each test case contains an integer 
# N
# N.
# The second line contains 
# N
# N space-separated integers 
# A
# 1
# ,
# A
# 2
# ,
# …
# ,
# A
# N
# A 
# 1
# ​
#  ,A 
# 2
# ​
#  ,…,A 
# N
# ​
#  .
# The third line contains 
# N
# N space-separated integers 
# B
# 1
# ,
# B
# 2
# ,
# …
# ,
# B
# N
# B 
# 1
# ​
#  ,B 
# 2
# ​
#  ,…,B 
# N
# ​
#  .
# Output Format
# For each test case, output on a new line - the maximum number of small indices you can get.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 3
# ≤
# N
# ≤
# 3000
# 3≤N≤3000
# 1
# ≤
# A
# i
# ,
# B
# i
# ≤
# 2
# ⋅
# N
# 1≤A 
# i
# ​
#  ,B 
# i
# ​
#  ≤2⋅N
# The sum of 
# N
# N over all test cases won't exceed 
# 3000
# 3000.
# Sample 1:
# Input
# Output
# 2
# 5
# 1 1 1 4 6
# 1 1 3 6 10
# 5
# 1 1 3 6 10
# 1 1 1 5 9
# 2
# 1
# Explanation:
# Test case 
# 1
# 1: It is optimal to choose 
# C
# =
# [
# 1
# ,
# 1
# ,
# 3
# ,
# 4
# ,
# 6
# ]
# C=[1,1,3,4,6].

# Test case 
# 2
# 2: It is optimal to choose 
# C
# =
# [
# 1
# ,
# 1
# ,
# 1
# ,
# 5
# ,
# 9
# ]
# C=[1,1,1,5,9].


# code for above problem statement
# '''

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of three lines of input.
The first line of each test case contains an integer 
N
N.
The second line contains 
N
N space-separated integers 
A
1
,
A
2
,
…
,
A
N
A 
1
​
 ,A 
2
​
 ,…,A 
N
​
 .
The third line contains 
N
N space-separated integers 
B
1
,
B
2
,
…
,
B
N
B 
1
​
 ,B 
2
​
 ,…,B 
N
​
 .
Output Format
For each test case, output on a new line - the maximum number of small indices you can get.


# '''

input
2
5
1 1 1 4 6
1 1 3 6 10
5
1 1 3 6 10
1 1 1 5 9

ouptut
2
1

code 

def solve():
 n = int(input())
 a = list(map(int, input().split()))
 b = list(map(int, input().split()))
 c = 0
 for i in range(n):
  if a[i] < b[i]:
   c += 1
   print(c)
   solve()
   else
   print(c)
   solve()
   