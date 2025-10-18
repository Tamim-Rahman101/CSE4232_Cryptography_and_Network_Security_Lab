import string
import random

def read_key(file):
    with open(file, "r") as file:
        return file.read()

def write_key(file, key):
    with open(file, "w") as file:
        file.write(key)

def generate_key(key_file1, key_file2, length):
    key = ""
    letters = string.ascii_uppercase
    for i in range(length):
        key += random.choice(letters)
    print(key)
    write_key(key_file1, key)
    write_key(key_file2, key)

def encrypt(plain_text, key_file):
    key = read_key(key_file)
    cipher_text = ""
    idx = 0
    for ch in plain_text:
        x = (ord(ch) + ord(key[idx])) % 26
        idx += 1
        cipher_text += chr(ord('A') + x)
    key = key[idx:]
    write_key(key_file, key)
    return cipher_text

def decrypt(cipher_text, key_file):
    key = read_key(key_file)
    plain_text = ""
    idx = 0
    for ch in cipher_text:
        x = (ord(ch) - ord(key[idx])) % 26
        idx += 1
        plain_text += chr(ord('A') + x)
    key = key[idx:]
    write_key(key_file, key)
    return plain_text

key_file1 = "onetimepad1"
key_file2 = "onetimepad2"
generate_key(key_file1, key_file2, 20)

original_text = "TAMIM"

cipher_text = encrypt(original_text, key_file1)
print(cipher_text)

plain_text = decrypt(cipher_text, key_file2)
print(plain_text)