def encrypt(plain_text, shift):
    result = ""
    for ch in plain_text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)

if __name__ == "__main__":
    text = input("Enter plaintext: ")
    shift = int(input("Enter shift value: "))
    encrypted = encrypt(text, shift)
    print(f"Encrypted: {encrypted}")
    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")
