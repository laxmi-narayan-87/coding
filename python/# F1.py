# F1. Game in Tree (Easy Version)
# time limit per test4 seconds
# memory limit per test256 megabytes
# This is the easy version of the problem. In this version, u=v
# . You can make hacks only if both versions of the problem are solved.

# Alice and Bob are playing a fun game on a tree. This game is played on a tree with n
#  vertices, numbered from 1
#  to n
# . Recall that a tree with n
#  vertices is an undirected connected graph with n−1
#  edges.

# Alice and Bob take turns, with Alice going first. Each player starts at some vertex.

# On their turn, a player must move from the current vertex to a neighboring vertex that has not yet been visited by anyone. The first player who cannot make a move loses.

# You are given two vertices u
#  and v
# . Represent the simple path from vertex u
#  to v
#  as an array p1,p2,p3,…,pm
# , where p1=u
# , pm=v
# , and there is an edge between pi
#  and pi+1
#  for all i
#  (1≤i<m
# ).

# You need to determine the winner of the game if Alice starts at vertex 1
#  and Bob starts at vertex pj
#  for each j
#  (where 1≤j≤m
# ).

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each test case contains a single integer n
#  (2≤n≤2⋅105
# ) — the number of vertices in the tree.

# Each of the following n−1
#  lines contains two integers a
#  and b
#  (1≤a,b≤n
# ), denoting an undirected edge between vertices a
#  and b
# . It is guaranteed that these edges form a tree.

# The last line of each test case contains two integers u
#  and v
#  (2≤u,v≤n
# , u=v
# ).

# It is guaranteed that the path from u
#  to v
#  does not pass through vertex 1
# .

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output m
#  lines.

# In the i
# -th line, print the winner of the game if Alice starts at vertex 1
#  and Bob starts at vertex pi
# . Print "Alice" (without quotes) if Alice wins, or "Bob" (without quotes) otherwise.

# Example
# InputCopy
# 3
# 3
# 1 2
# 2 3
# 2 2
# 3
# 1 2
# 2 3
# 3 3
# 6
# 1 2
# 1 3
# 2 4
# 2 5
# 1 6
# 4 4
# OutputCopy
# Bob
# Alice
# Alice
# Note
# Tree from the first and second examples.
# In the first test case, the path will be (2,2
# ). Bob starts at vertex 2
# , Alice will not be able to move anywhere on her first turn and will lose.

# In the second test case, the path will be (3,3
# ). Bob starts at vertex 3
# , Alice will move to vertex 2
# , and Bob will have no remaining vertices to visit and will lose.


CODE FOR ABOVE PRONLEM STATEMENT

def solve():
    n = int(input())
    adj = [[] for _ in range(n)]
    for i in range(n):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        for i in range(n):
            adj[i].sort())
        if v in adj[u]:
            print("Bob")
        else:
            print("Alice")
for _ in range(int(input())):
    solve()

