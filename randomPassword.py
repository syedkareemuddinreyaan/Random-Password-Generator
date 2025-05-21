import random
import string

password_len = 6
charValues = string.ascii_letters + string.digits + string.punctuation


password = ""
for i in range(password_len):
    password += random.choice(charValues)

print(f"your random password is: {password}")
'''
this can also be done using list comprehension like
password = "".join([random.choice(charValues) for i in range(password_len)])
print(password)
'''