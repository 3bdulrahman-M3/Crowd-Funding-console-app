import json
import os
from datetime import datetime
from utils import validate_date

PROJECTS_FILE = 'projects.json'

def load_projects():
    if not os.path.exists(PROJECTS_FILE):
        return []
    with open(PROJECTS_FILE, 'r') as f:
        return json.load(f)

def save_projects(projects):
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=2)

def project_menu(user):
    while True:
        print("\n--- Project Menu ---")
        print("1. Create Project")
        print("2. View All Projects")
        print("3. Edit My Project")
        print("4. Delete My Project")
        print("5. Search Projects by Date")
        print("6. Logout")
        choice = input("Select an option: ")
        if choice == '1':
            create_project(user)
        elif choice == '2':
            view_projects()
        elif choice == '3':
            edit_project(user)
        elif choice == '4':
            delete_project(user)
        elif choice == '5':
            search_projects_by_date()
        elif choice == '6':
            break
        else:
            print("Invalid option. Try again.")

def create_project(user):
    print("\n--- Create Project ---")
    title = input("Title: ")
    details = input("Details: ")
    target = input("Total target (EGP): ")
    try:
        target = float(target)
    except ValueError:
        print("Invalid target amount.")
        return
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    start = validate_date(start_date)
    end = validate_date(end_date)
    if not start or not end or end <= start:
        print("Invalid date(s) or end date before start date.")
        return
    projects = load_projects()
    project = {
        'id': len(projects) + 1,
        'owner': user['email'],
        'title': title,
        'details': details,
        'target': target,
        'start_date': start_date,
        'end_date': end_date
    }
    projects.append(project)
    save_projects(projects)
    print("Project created successfully!")

def view_projects():
    print("\n--- All Projects ---")
    projects = load_projects()
    if not projects:
        print("No projects found.")
        return
    for p in projects:
        print(f"ID: {p['id']} | Title: {p['title']} | Owner: {p['owner']} | Target: {p['target']} EGP | {p['start_date']} to {p['end_date']}")
        print(f"Details: {p['details']}")
        print("-"*40)

def edit_project(user):
    projects = load_projects()
    my_projects = [p for p in projects if p['owner'] == user['email']]
    if not my_projects:
        print("You have no projects to edit.")
        return
    for p in my_projects:
        print(f"ID: {p['id']} | Title: {p['title']}")
    pid = input("Enter project ID to edit: ")
    for p in projects:
        if str(p['id']) == pid and p['owner'] == user['email']:
            print("Leave blank to keep current value.")
            title = input(f"Title [{p['title']}]: ") or p['title']
            details = input(f"Details [{p['details']}]: ") or p['details']
            target = input(f"Target [{p['target']}]: ") or p['target']
            try:
                target = float(target)
            except ValueError:
                print("Invalid target amount.")
                return
            start_date = input(f"Start date [{p['start_date']}]: ") or p['start_date']
            end_date = input(f"End date [{p['end_date']}]: ") or p['end_date']
            start = validate_date(start_date)
            end = validate_date(end_date)
            if not start or not end or end <= start:
                print("Invalid date(s) or end date before start date.")
                return
            p['title'] = title
            p['details'] = details
            p['target'] = target
            p['start_date'] = start_date
            p['end_date'] = end_date
            save_projects(projects)
            print("Project updated.")
            return
    print("Project not found or not owned by you.")

def delete_project(user):
    projects = load_projects()
    my_projects = [p for p in projects if p['owner'] == user['email']]
    if not my_projects:
        print("You have no projects to delete.")
        return
    for p in my_projects:
        print(f"ID: {p['id']} | Title: {p['title']}")
    pid = input("Enter project ID to delete: ")
    for i, p in enumerate(projects):
        if str(p['id']) == pid and p['owner'] == user['email']:
            del projects[i]
            save_projects(projects)
            print("Project deleted.")
            return
    print("Project not found or not owned by you.")

def search_projects_by_date():
    date_str = input("Enter date to search (YYYY-MM-DD): ")
    date = validate_date(date_str)
    if not date:
        print("Invalid date format.")
        return
    projects = load_projects()
    found = False
    for p in projects:
        start = validate_date(p['start_date'])
        end = validate_date(p['end_date'])
        if start and end and start <= date <= end:
            print(f"ID: {p['id']} | Title: {p['title']} | Owner: {p['owner']} | Target: {p['target']} EGP | {p['start_date']} to {p['end_date']}")
            print(f"Details: {p['details']}")
            print("-"*40)
            found = True
    if not found:
        print("No projects found for this date.") 