import random
import string
import itertools


def generate_substitution_pairs(n):
    letters = string.ascii_uppercase
    substitution = {}
    for l in range(1, n+1):
        sequences = [''.join(p) for p in itertools.product(letters, repeat=l)]
        shuffled = sequences.copy()
        random.shuffle(shuffled)
        
        for plain, cipher in zip(sequences, shuffled):
            substitution[plain] = cipher

    return substitution


def encrypt(plaintext, substitution, n):
    plaintext = plaintext.upper().replace(" ", "")
    cipher_text = ""

    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)

    for i in range(0, len(plaintext), n):
        block = plaintext[i:i+n]
        cipher_text += substitution.get(block, block)

    return cipher_text


def decrypt(cipher_text, substitution, n):
    reverse_sub = {v: k for k, v in substitution.items()}
    plain_text = ""

    for i in range(0, len(cipher_text), n):
        block = cipher_text[i:i+n]
        plain_text += reverse_sub.get(block, block)

    return plain_text


n = 3
substitution = generate_substitution_pairs(n)

plaintext = "HELLOTHERE"
cipher_text = encrypt(plaintext, substitution, n)
decrypted_text = decrypt(cipher_text, substitution, n)

print(f"\nPlaintext:  {plaintext}")
print(f"Ciphertext: {cipher_text}")
print(f"Decrypted:  {decrypted_text}")
