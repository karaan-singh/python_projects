text = input("Enter text or number to check for palindrome: ")

cleaned = str(text).replace(" ", "").lower()
is_palindrome = True

for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")