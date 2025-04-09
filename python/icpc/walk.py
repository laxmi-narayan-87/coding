import sys
input = sys.stdin.read

def train_or_walk():
    data = input().split()
    T = int(data[0])
    idx = 1
    results = []

    for _ in range(T):
        N = int(data[idx])
        A = int(data[idx + 1]) - 1
        B = int(data[idx + 2]) - 1
        C = int(data[idx + 3]) - 1
        D = int(data[idx + 4]) - 1
        P = int(data[idx + 5])
        Q = int(data[idx + 6])
        Y = int(data[idx + 7])

        coords = list(map(int, data[idx + 8: idx + 8 + N]))
        idx += 8 + N

        x_A, x_B, x_C, x_D = coords[A], coords[B], coords[C], coords[D]

        walk_time = abs(x_B - x_A) * P
        min_time = walk_time

        time_to_C = abs(x_C - x_A) * P

        if time_to_C <= Y:
            train_time = abs(x_D - x_C) * Q
            remaining_walk = abs(x_B - x_D) * P
            total_time_with_train = Y + train_time + remaining_walk
            min_time = min(min_time, total_time_with_train)

        results.append(str(min_time))

    sys.stdout.write("\n".join(results) + "\n")

train_or_walk()
