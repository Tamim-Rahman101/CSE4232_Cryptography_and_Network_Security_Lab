# MD5 (Message Digest Algorithm 5) is a cryptographic 
# hash function that takes any input data and 
# produces a fixed 128-bit (16-byte) hash value.

# each hexadecimal character takes 4 bit
# thus 32 * 4 = 128 bit

import hashlib

def md5(data):
    return hashlib.md5(data.encode()).hexdigest()

data = "cseRu"
md5_hash = md5(data)
print(f"Original data: {data}")
print(f"Hash value: {md5_hash}")

data = "cseru"
md5_hash = md5(data)
print(f"Alterd data: {data}")
print(f"Hash value: {md5_hash}")