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
first_cipher_text = encrypt(original_text, key)
print(first_cipher_text)
second_cipher_text = encrypt(first_cipher_text, key)
print(second_cipher_text)
second_plain_text = decrypt(second_cipher_text, key)
print(second_plain_text)
first_plain_text = decrypt(first_cipher_text, key)
print(first_plain_text)

