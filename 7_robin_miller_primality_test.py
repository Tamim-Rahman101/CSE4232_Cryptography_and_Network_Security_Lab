import random

def prime_test(n, t):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    
    # select m, k such that n - 1 = 2^k * m
    m = n - 1
    k = 0
    while m % 2 == 0:
        m = m // 2
        k += 1
    

    for i in range(t):
        a = random.randint(2, n - 2)
        b = pow(a, m, n)    # b0 = a^m % n

        if b == 1 or b == n - 1:    # probably prime
            continue

        for j in range(k - 1):
            b = pow(b, 2, n)    # b(i+1) = bi^2 % n
            if b == n - 1:  # if for any k, b = n - 1 then its probably prime
                break
        else:               # if we dont get any b = n - 1 then its composite
            return False
    
    return True

n = 19

if prime_test(n, 10):
    print(f"{n} is probably prime")
else:
    print(f"{n} is composite")

