def construct_coprime_array(T, test_cases):
    import math
    from itertools import count

    # Helper function to generate prime numbers
    def generate_primes(limit):
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        primes = []
        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        return primes

    # Generate primes up to 2 * 10^6
    primes = generate_primes(2 * 10**6)

    results = []
    for n, k in test_cases:
        # Maximum possible pairs
        max_pairs = n * (n - 1) // 2
        if k > max_pairs:
            results.append("-1")
            continue

        # Construct the array
        arr = []
        remaining_pairs = k

        # Use prime numbers to maximize co-prime pairs
        for p in primes:
            arr.append(p)
            if len(arr) == n:
                break

        # If fewer pairs are required, introduce non-co-prime numbers
        i = 0
        while remaining_pairs < max_pairs:
            arr[i % n] *= primes[0]  # Introduce a common factor
            i += 1
            max_pairs -= 1

        results.append(" ".join(map(str, arr)))

    return results


# Input handling
if __name__ == "__main__":
    T = int(input())  # Number of test cases
    test_cases = []
    for _ in range(T):
        N, K = map(int, input().split())
        test_cases.append((N, K))

    results = construct_coprime_array(T, test_cases)
    for res in results:
        print(res)


#4
# 5 10
# 4 13
# 2 1
# 6 7

#output
# 6 19 85 77 3887
# -1
# 2 3
# 5 2 2 7 10 50 