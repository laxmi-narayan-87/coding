def solve():
    T = int(input())
    results = []
    for _ in range(T):
        N, K = map(int, input().split())
        array = list(map(int, input().split()))
        array = [a for a in array if (a & K) == K]
        N = len(array)
        found = False
        for mask in range(1, 1 << N):
            current_and = -1
            indices = []
            for i in range(N):
                if mask & (1 << i):
                    if current_and == -1:
                        current_and = array[i]
                    else:
                        current_and &= array[i]
                    indices.append(i + 1)
            if current_and == K:
                results.append("YES")
                results.append(str(len(indices)))
                results.append(" ".join(map(str, indices)))
                found = True
                break
        if not found:
            results.append("NO")
    print("\n".join(results))




# use this input and output to test the code
# input 
# 2
# 5 10
# 11 12 13 14 15
# 4 1023
# 511 512 256 255

# #output
# YES
# 3
# 1 4 5
# NO



