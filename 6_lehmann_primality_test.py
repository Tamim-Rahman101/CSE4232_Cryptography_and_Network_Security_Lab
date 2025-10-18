import random

def prime_test(n, t):
    if n <= 2:
        return n == 2
    
    for i in range(t):
        a = random.randint(2, n-2)
        e = (n-1) // 2
        res = pow(a, e, n)
        if res != 1 and res != n - 1:
            return False
        
    return True

n = int(input("Enter a number: "))
if prime_test(n, 100):
    print(f"{n} is probably prime")
else:
    print(f"{n} is composite")