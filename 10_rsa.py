import math

def gcd(a, b):
    while b != 0:
        a = b
        b = a % b
    return a
    
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa(p, q):
    print(f"p = {p}, q = {q}")
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(2, phi-1):
        if math.gcd(e, phi) == 1:
            break
    print(f"e = {e}")

    d = mod_inverse(e, phi)
    print(f"d = {d}")

    print(f"Public key: (e={e}, n={n})")
    print(f"Public key: (d={d}, n={n})")
    return (e,n), (d,n)

def encrypt(msg, public_key):
    e, n = public_key
    msg_str = str(msg)
    msg_blocks = [int(msg_str[i:i+3]) for i in range(0, len(msg_str), len(str(n)) - 1)]
    cipher_blocks = [pow(m, e, n) for m in msg_blocks]
    return cipher_blocks

def decrypt(cipher_blocks, private_key):
    d, n = private_key
    decrypted_blocks = [pow(c, d, n) for c in cipher_blocks]
    decrypted_msg = "".join(str(m).zfill(len(str(n)) - 1) for m in decrypted_blocks)
    return decrypted_msg

p = 47
q = 71
public_key, private_key = rsa(p, q)

message = 6882326879666683
print("Original message: ", message)

cipher_blocks = encrypt(message, public_key)
print("Cipher blocks: ", cipher_blocks)

decrypted_message = decrypt(cipher_blocks, private_key)
print("Decrypted message: ", decrypted_message)