import random
import string

length = int(input("Enter password length: "))

digits = string.digits
password = ''.join(random.choice(digits) for _ in range(length))

print(f"Generated numeric password: {password}")