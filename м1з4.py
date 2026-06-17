def xor_cipher(text, key):

  key_bytes = (key * (len(text) // len(key) + 1))[:len(text)]
  return bytes([ord(t) ^ ord(k) for t, k in zip(text, key_bytes)])

def xor_decipher(ciphertext, key):

  key_bytes = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
  return bytes([c ^ ord(k) for c, k in zip(ciphertext, key_bytes)]).decode('utf-8')

message = "Прикладная информатика"
key = "key"
encoded = xor_cipher(message, key)
decoded = xor_decipher(encoded, key)

print("Исходное:", message)
print("Зашифрованное (байты):", encoded)
print("Расшифрованное:", decoded)
