# enumerate all primes to N
# given n, return all primes up to and including n

def generate_primes(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)

    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            
            # sieve out p's multiples
            for i in range(p, n + 1, p):
                is_prime[i] = False

    return primes
    
# test n = 100
print(generate_primes(100))
