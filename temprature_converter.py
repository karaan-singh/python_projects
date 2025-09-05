print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = input("Enter choice (1/2/3/4/5/6): ")
temp = float(input("Enter temperature value: "))

if choice == '1':
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result}°F")
elif choice == '2':
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result}°C")
elif choice == '3':
    result = temp + 273.15
    print(f"{temp}°C = {result}K")
elif choice == '4':
    result = temp - 273.15
    print(f"{temp}K = {result}°C")
elif choice == '5':
    result = (temp - 32) * 5/9 + 273.15
    print(f"{temp}°F = {result}K")
elif choice == '6':
    result = (temp - 273.15) * 9/5 + 32
    print(f"{temp}K = {result}°F")
else:
    print("Invalid choice.")