import re
import json
import os
from utils import validate_phone_number, validate_email

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def register():
    print("\n--- Registration ---")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    while True:
        email = input("Email: ")
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")
    while True:
        password = input("Password: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            break
        print("Passwords do not match. Please try again.")
    while True:
        phone = input("Mobile phone: ")
        if validate_phone_number(phone):
            break
        print("Invalid phone number. Please try again.")
    users = load_users()
    if any(u['email'] == email for u in users):
        print("Email already registered.")
        return
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'phone': phone
    }
    users.append(user)
    save_users(users)
    print("Registration successful! You can now login.")

def login():
    print("\n--- Login ---")
    while True:
        email = input("Email: ")
        password = input("Password: ")
        users = load_users()
        for user in users:
            if user['email'] == email and user['password'] == password:
                print(f"Welcome, {user['first_name']}!")
                return user
        print("Invalid email or password. Please try again.")
        retry = input("Do you want to try again? (y/n): ").strip().lower()
        if retry != 'y':
            return None 