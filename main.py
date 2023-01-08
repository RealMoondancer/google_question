def solution(n):
    str_len = n + 5
    max_int = int(str_len * (5000/2465)+475)

    num_set = [True] * max_int
    num_set[0] = False
    num_set[1] = False

    max_check = int(max_int ** 0.5) # Why compute the maximum number to check each loop? Its always the same

    for num, prime in enumerate(num_set):
        if prime and num <= max_check:
            for i in range(num ** 2, max_int, num):
                num_set[i] = False

    p_str = ''.join([str(i) for i, prime in enumerate(num_set) if prime])
    return p_str[n:n+5]

import time

start = time.time()
for i in range(10000):
    solution(10000)

print(time.time() - start)
