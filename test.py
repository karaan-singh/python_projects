import mysql.connector

# Ensure the credentials are correct
# Replace 'your_password_here' with the actual password for the 'root' user
# If you are unsure of the password, reset it in MySQL
password="your_password_here"  # Update this line with the correct password

# connect to mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,  # Use the updated password variable
    database="python_test"
)

cursor = db.cursor()

name = "Karan"
age = 22

sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
values = (name, age)

cursor.execute(sql, values)

db.commit()

print("Data inserted successfully")