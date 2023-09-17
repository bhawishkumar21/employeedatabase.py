import sqlite3

connection = sqlite3.connect("Employee.sqlite")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Employee (emp_id TEXT, emp_name TEXT)""")
connection.commit()

while True:
    print("1. To Enter Your Data")
    print("2. To View Data")
    print("3. To END")
    choice = input("Enter Your Choice:")

    if choice == "1":
        emp_id = input("Enter Employee Id:")
        emp_name = input("Enter Employee Name:") 
        cursor.execute("INSERT INTO Employee (emp_id, emp_name) VALUES (?, ?)", (emp_id, emp_name))
        connection.commit()
        print("Data Entered Successfully")

    elif choice == "2":
        cursor.execute("SELECT * FROM Employee")
        print("Employee ID\tEmployee Name")
        for row in cursor:
            print(f"{row[0]}\t\t{row[1]}")

    elif choice == "3":
        break

connection.close()
