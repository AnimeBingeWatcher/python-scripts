import random
import string
import uuid

filename = str(uuid.uuid4())
password = ''.join(random.choice(string.printable) for i in range(20))

file = open(f"{filename}.txt", "x", encoding="utf-8")
file.write(password)

file = open(f"{filename}.txt", "r", encoding="utf-8")

print(file.read())
