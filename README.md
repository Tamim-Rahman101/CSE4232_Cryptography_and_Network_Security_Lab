# CSE4232: Cryptography and Network Security Lab

This repository contains the lab works of **CSE4232 – Cryptography and Network Security Lab** course.  
All programs are implemented in **Python** with clear encryption and decryption processes demonstrated for each algorithm.

---

## Lab Experiments

### 1. Caesar Cipher
- Implemented the **Caesar Cipher** (shift of 3).
- Performed encryption and decryption to retrieve the original plaintext.

### 2. Polygram Substitution Cipher
- Implemented **Polygram Cipher** with a block size of 3.
- Encrypted plaintext by substituting character blocks.
- Reversed operation to recover the plaintext.

### 3. Transposition Cipher
- Implemented **Columnar Transposition Cipher**.
- User inputs the **width (key)** to determine column arrangement.
- Performed both encryption and decryption.

### 4. Double Transposition Cipher
- Applied **two successive transposition ciphers** using two keys.
- Verified correct decryption of ciphertext back to original text.

### 5. One Time Pad (OTP)
- Used a **truly random nonrepeating key file**.
- Implemented **bitwise XOR** for encryption and decryption.
- Verified perfect secrecy property.

### 6. Lehmann Primality Test
- Implemented **Lehmann’s algorithm** to determine if a number *P* is prime.

### 7. Rabin–Miller Primality Test
- Implemented the **Rabin–Miller probabilistic primality test**.
- Compared performance and accuracy with Lehmann’s test.

### 8. MD5 Hash Function
- Implemented **MD5 one-way hash** algorithm.
- Demonstrated how the same input produces identical 128-bit hash values.

### 9. Secure Hash Algorithm (SHA)
- Implemented **SHA-1/SHA-256** one-way hashing.
- Compared with MD5 in terms of hash length and security.

### 10. RSA Algorithm
- Implemented **RSA public-key cryptosystem**.
- Supported both **integer** and **string (ASCII converted)** plaintexts.
- Demonstrated encryption and decryption using generated keys.

### 11. Diffie–Hellman Key Exchange
- Simulated **secure key exchange** between two users over an insecure channel.
- Illustrated the concept of **shared secret generation**.

### 12. Pretty Good Privacy (PGP) (not implemented yet)
- Implemented simplified **PGP operations**:
  - **Authentication** (Digital signature simulation)
  - **Confidentiality** (Hybrid encryption using symmetric + asymmetric keys)
- Demonstrated full data transmission workflow.

---