import random
import string
import uuid

myfile = "b.txt" 

filename = str(uuid.uuid4())
password = ''.join(random.choice(string.printable) for i in range(20))

file = open(myfile.replace("b", filename), "x", encoding="utf-8")
    
file = open(myfile.replace("b", filename), "w", encoding="utf-8")
file.write(password)

file = open(myfile.replace("b", filename), "r", encoding="utf-8")

print(file.read())
