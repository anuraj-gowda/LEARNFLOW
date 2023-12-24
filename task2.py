import hashlib
import json
import random
from getpass import getpass

class PasswordManager:
    def _init_(self):
        self.passwords = {}
        self.master_password_hash = None
        self.file_path = "passwords.json"

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()

    def set_master_password(self):
        # Set the master password
        master_password = getpass("Set your master password: ")
        self.master_password_hash = self.hash_password(master_password)
        print("Master password set successfully!")

    def authenticate_master_password(self):
        # Authenticate the master password
        attempts = 3
        while attempts > 0:
            entered_password = getpass("Enter your master password: ")
            entered_password_hash = self.hash_password(entered_password)
            if entered_password_hash == self.master_password_hash:
                print("Authentication successful!")
                return True
            else:
                attempts -= 1
                print(f"Wrong password! {attempts} attempts remaining.")
        print("Authentication failed. Exiting.")
        return False

    def generate_password(self, length=12):
        # Generate a random password with letters, digits, and symbols
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def add_password(self, category, website, username, password):
        # Add a password to the manager
        if category not in self.passwords:
            self.passwords[category] = {}
        self.passwords[category][website] = {'username': username, 'password': password}
        print(f"Password for {website} added to {category} category.")
        self.save_passwords()

    def get_password(self, category, website):
        # Retrieve a password securely
        if category in self.passwords and website in self.passwords[category]:
            return self.passwords[category][website]['password']
        else:
            print(f"No password found for {website} in {category} category.")

    def list_categories(self):
        # List all categories
        print("Categories:")
        for category in self.passwords:
            print(f"- {category}")

    def list_passwords(self, category):
        # List all passwords in a category
        if category in self.passwords:
            print(f"Passwords in {category} category:")
            for website in self.passwords[category]:
                print(f"- {website}")
        else:
            print(f"No passwords found in {category} category.")

    def delete_password(self, category, website):
        # Delete a password
        if category in self.passwords and website in self.passwords[category]:
            del self.passwords[category][website]
            print(f"Password for {website} in {category} category deleted.")
            self.save_passwords()
        else:
            print(f"No password found for {website} in {category} category.")

    def save_passwords(self):
        # Save passwords to a file
        with open(self.file_path, 'w') as file:
            json.dump(self.passwords, file)
        print("Passwords saved successfully.")

    def load_passwords(self):
        # Load passwords from a file
        try:
            with open(self.file_path, 'r') as file:
                self.passwords = json.load(file)
            print("Passwords loaded successfully.")
        except FileNotFoundError:
            print("No saved passwords found.")

if _name_ == "_main_":
    # Create an instance of PasswordManager
    password_manager = PasswordManager()

    # Load saved passwords
    password_manager.load_passwords()

    # Set the master password
    password_manager.set_master_password()

    # Authenticate the master password
    if password_manager.authenticate_master_password():
        while True:
            print("\nOptions:")
            print("1. Add Password")
            print("2. Retrieve Password")
            print("3. List Categories")
            print("4. List Passwords in Category")
            print("5. Delete Password")
            print("6. Save and Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                category = input("Enter the category: ")
                website = input("Enter the website: ")
                username = input("Enter the username: ")
                password = input("Enter the password (or press Enter to generate one): ")
                if not password:
                    password = password_manager.generate_password()
                password_manager.add_password(category, website, username, password)

            elif choice == "2":
                category = input("Enter the category: ")
                website = input("Enter the website: ")
                retrieved_password = password_manager.get_password(category, website)
                print(f"Retrieved Password: {retrieved_password}")

            elif choice == "3":
                password_manager.list_categories()

            elif choice == "4":
                category = input("Enter the category: ")
                password_manager.list_passwords(category)

            elif choice == "5":
                category = input("Enter the category: ")
                website = input("Enter the website: ")
                password_manager.delete_password(category, website)

            elif choice == "6":
                password_manager.save_passwords()
                print("Exiting.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")