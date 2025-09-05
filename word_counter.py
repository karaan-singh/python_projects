text = input("Enter a string: ")
if not text.strip():
    print("No input provided.")
else:
    words = text.split()
    count = len(words)
    print(f"Word count: {count}")