import random
import string
import math

def generate_password(length=12):
  chars = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(chars) for _ in range(length))
  return password

def entropy(password):
  pool_size = 0
  if any(c.islower() for c in password):
    pool_size += 26
  if any(c.isupper() for c in password):
    pool_size += 26
  if any(c.isdigit() for c in password):
    pool_size += 10
  if any(c in string.punctuation for c in password):
    pool_size += len(string.punctuation)

  if pool_size == 0:
    return 0, "очень слабый"

  ent = len(password) * math.log2(pool_size)

  if ent < 40:
    strength = "слабый"
  elif ent < 60:
    strength = "средний"
  else:
    strength = "сильный"

return ent, strength
pwd = generate_password(10)
e, s = entropy(pwd)
print(f"Пароль: {pwd}\nЭнтропия: {e:.2f} бит\nСтойкость: {s}")
