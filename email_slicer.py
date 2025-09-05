email = input("Enter your email address: ")

if "@" in email:
    username, domain = email.split("@", 1)
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address.")