import sys
from bisect import bisect_left, bisect_right

def generate_periodic_numbers(limit):
    periodic_numbers = set()
    for bits in range(1, 31):
        for pattern in range(1, (1 << bits)):
            num = pattern
            while num <= limit:
                periodic_numbers.add(num)
                num = (num << bits) | pattern
    return sorted(periodic_numbers)

LIMIT = 10**9
periodic_numbers = generate_periodic_numbers(LIMIT)

def count_periodic_numbers_in_range(L, R):
    return bisect_right(periodic_numbers, R) - bisect_left(periodic_numbers, L)

input = sys.stdin.read
data = input().split()
T = int(data[0])
output = []
idx = 1
for _ in range(T):
    L = int(data[idx])
    R = int(data[idx + 1])
    output.append(str(count_periodic_numbers_in_range(L, R)))
    idx += 2

sys.stdout.write("\n".join(output) + "\n")
