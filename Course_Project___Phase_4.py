# Darrell Lawson
# CIS261
# Project Part 4

import getpass

# Create a function to create a new user
def create_user():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    role = input("Enter role (user/admin): ")
    with open("users.txt", "a") as f:
        f.write(f"{username} {password} {role}\n")
    print("User created successfully!")

# Create a function to login
def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    with open("users.txt", "r") as f:
        for line in f:
            u, p, r = line.strip().split()
            if u == username and p == password:
                print(f"Logged in as {username} ({r})")
                return username, r
    print("Invalid username or password")
    return None, None

# Create a function to add an employee
def add_employee():
    name = input("Enter employee name: ")
    start_date = input("Enter start date (MM/DD/YYYY): ")
    end_date = input("Enter end date (MM/DD/YYYY): ")
    hours_worked = input("Enter hours worked: ")
    pay_amount = input("Enter pay amount: ")
    tax_rate = input("Enter tax rate: ")
    with open("Employees.txt", "a") as f:
        f.write(f"{name},{start_date},{end_date},{hours_worked},{pay_amount},{tax_rate}\n")
    print("Employee added successfully!")

# Create a function to view employees (only for admins)
def view_employees(username):
    with open("users.txt", "r") as f:
        for line in f:
            values = line.strip().split()
            if len(values) >= 3:
                u, _, r = values
                if u == username and r == "admin":
                    with open("Employees.txt", "r") as f:
                        print(f.read())


# Main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Create a user")
    print("2. Login")
    print("3. Add an employee")
    print("4. View employees (admin only)")
    print("5. Exit")
    choice = input("> ")

    if choice == "1":
        create_user()
    elif choice == "2":
        username, role = login()
        if username is not None and role is not None:
            while True:
                print("\nWhat would you like to do?")
                print("1. Add an employee")
                print("2. View employees (admin only)")
                print("3. Logout")
                choice = input("> ")

                if choice == "1":
                    add_employee()
                elif choice == "2":
                    if role == "admin":
                        view_employees(username)
                    else:
                        print("You do not have permission to view employees")
                elif choice == "3":
                    break
                else:
                    print("Invalid choice")
    elif choice == "3":
        add_employee()
    elif choice == "4":
        if role == "admin":
            view_employees(username)
        else:
            print("You do not have permission to view employees")
    elif choice == "5":
        break
    else:
        print("Invalid choice")
