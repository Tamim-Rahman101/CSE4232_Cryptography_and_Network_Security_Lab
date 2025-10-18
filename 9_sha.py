import hashlib

def sha(data, algo):
    if algo == 'sha1': return hashlib.sha1(data.encode()).hexdigest()
    elif algo == 'sha256': return hashlib.sha256(data.encode()).hexdigest()
    elif algo == 'sha512': return hashlib.sha512(data.encode()).hexdigest()


data = "cseRu"
sha1 = sha(data, 'sha1')
sha256 = sha(data, 'sha256')
# sha512 = sha(data, 'sha512')
print(f"Original data: {data}")
print(f"Hash value: {sha1}")
print(f"Hash value: {sha256}")
# print(f"Hash value: {sha512}")

data = "cseru"
sha1 = sha(data, 'sha1')
sha256 = sha(data, 'sha256')
# sha512 = sha(data, 'sha512')
print(f"Original data: {data}")
print(f"Hash value: {sha1}")
print(f"Hash value: {sha256}")
# print(f"Hash value: {sha512}")
