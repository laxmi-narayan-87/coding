def maximize_sum(arr, n):
    arr.sort()
    rearranged = []
    i, j = 0, n - 1
    while i < j:
        rearranged.append(arr[i])
        rearranged.append(arr[j])
        i += 1
        j -= 1
    max_sum = 0
    for k in range(0, n - 1, 2):
        max_sum += abs(rearranged[k] - rearranged[k + 1])
    
    return max_sum
import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])
index = 1
results = []
for _ in range(T):
    n = int(data[index])
    arr = list(map(int, data[index + 1:index + n + 1]))
    index += n + 1
    results.append(maximize_sum(arr, n))
sys.stdout.write("\n".join(map(str, results)) + "\n")
