import random
import string

pass_len=8
charValues= string.ascii_letters + string.digits + string.punctuation
print(charValues)
password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("Your random Password is: ", password)








