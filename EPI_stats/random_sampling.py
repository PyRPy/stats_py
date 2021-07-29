# 5.12 sample offline data

import random

def random_sampling(k, A):
    for i in range(k):
        r = random.randint(i, len(A) - i)
        A[i], A[r] = A[r], A[i]

# test
A = [3, 7, 5, 11]
k = 3

print(A)
for j in range(4):
    random_sampling(k, A)
    print(A)

