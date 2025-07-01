import auth
import projects
import utils

def main():
    while True:
        print("\n--- Crowd-Funding Console App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            auth.register()
        elif choice == '2':
            user = auth.login()
            if user:
                projects.project_menu(user)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main() 