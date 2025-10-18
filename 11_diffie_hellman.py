# Step 1: Publicly shared prime number (p) and base (g)
p = 7    # primitive root / base
n = 23   # prime number / mod n
print(f"Publicly shared values: p (primiptive root) = {p},  n (prime number) = {n}\n")


# Step 2: Each party chooses their private key (kept secret)
a = 3   # Alice's private key
b = 5   # Bob's private key
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}\n")


# Step 3: Each party computes their public key
A = pow(p, a, n)   # A = p^a mod n
B = pow(p, b, n)   # B = p^b mod n
print(f"Alice's public key (A): {A}")
print(f"Bob's public key (B): {B}\n")


# Step 4: Exchange public keys and compute shared secret
# Alice uses Bob's public key, Bob uses Alice's public key
shared_key_A = pow(B, a, n)   # K = B^a mod n
shared_key_B = pow(A, b, n)   # K = A^b mod n
print(f"Alice's computed shared key: {shared_key_A}")
print(f"Bob's computed shared key: {shared_key_B}\n")


# Step 5: Verify that both keys match
if shared_key_A == shared_key_B:
    print(f"Shared Secret Key Established: {shared_key_A}")
else:
    print("Key mismatch! Something went wrong.")
