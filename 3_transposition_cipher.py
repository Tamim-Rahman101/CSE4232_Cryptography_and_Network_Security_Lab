def encrypt(plaintext, key):
    plaintext = plaintext.replace(' ', '')
    length = len(plaintext)
    ciphertext = ""

    for k in range(key):
        for i in range(k, length, key):
            ciphertext += plaintext[i]
    return ciphertext

def decrypt(ciphertext, key):
    lenght = len(ciphertext)
    plaintext = [''] * lenght
    idx = 0

    for k in range(key):
        for i in range(k, lenght, key):
            plaintext[i] = ciphertext[idx]
            idx += 1
    return ''.join(plaintext)


# original_text = "department of computer science and engineering"
original_text = input("Enter the original text: ")
key = int(input("Enter the key: "))
cipher_text = encrypt(original_text, key)
print(cipher_text)
plain_text = decrypt(cipher_text, key)
print(plain_text)


# D  E  P  A
# R  T  M  E
# N  T

# | Step | k | i values (k, k+width, ...) | Picked letters | ciphertext so far |
# | ---- | - | -------------------------- | -------------- | ----------------- |
# | 1    | 0 | 0, 4, 8                    | D, R, N        | **DRN**           |
# | 2    | 1 | 1, 5, 9                    | E, T, T        | **DRNETT**        |
# | 3    | 2 | 2, 6                       | P, M           | **DRNETEPM**      |
# | 4    | 3 | 3, 7                       | A, E           | **DRNETEPMAE**    |

# | Step | k | i values | Cipher letters | plain_text after step |
# | ---- | - | -------- | -------------- | --------------------- |
# | 1    | 0 | 0, 4, 8  | D, R, N        | D _ _ _ R _ _ _ N _   |
# | 2    | 1 | 1, 5, 9  | E, T, T        | D E _ _ R T _ _ N T   |
# | 3    | 2 | 2, 6     | P, M           | D E P _ R T M _ N E   |
# | 4    | 3 | 3, 7     | A, E           | D E P A R T M E N E   |
