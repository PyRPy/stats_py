# permutations
# 5.10
def apply_permutation(perm, A):
    """
        perm: list
        A:    list

    """
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            
            A[perm[next]], A[i] = A[i], A[perm[next]]
            temp = perm[next]

            perm[next] -= len(perm)
            next = temp
            
    perm[:] = [a + len(perm) for a in perm]

# test code

perm = [1, 2, 3, 0]
A = [3, 5, 2, 4]

print(A)

apply_permutation(perm, A)

print(A)
