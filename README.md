# Crowd-Funding Console App

A Python-based console application for managing crowd-funding projects. This application allows users to register, login, create projects, and manage their crowd-funding campaigns through a simple command-line interface.

## Features

### User Management
- **User Registration**: Create new accounts with validation for email, phone number, and password confirmation
- **User Login**: Secure authentication system
- **Data Persistence**: User data stored in JSON format

### Project Management
- **Create Projects**: Add new crowd-funding projects with title, details, target amount, and date range
- **View All Projects**: Browse all available projects in the system
- **Edit Projects**: Modify existing projects (only project owners can edit their own projects)
- **Delete Projects**: Remove projects from the system (only project owners can delete their own projects)
- **Search by Date**: Find projects active on specific dates

### Data Validation
- **Email Validation**: Ensures proper email format
- **Phone Number Validation**: Validates Egyptian mobile numbers (01XXXXXXXXX format)
- **Date Validation**: Ensures proper date format and logical date ranges
- **Input Validation**: Comprehensive validation for all user inputs

## File Structure

```
Crowd-Funding console app/
├── main.py          # Main application entry point
├── auth.py          # Authentication and user management
├── projects.py      # Project management functionality
├── utils.py         # Utility functions and validators
├── users.json       # User data storage
├── projects.json    # Project data storage
└── README.md        # This file
```

## Installation

1. **Prerequisites**: Ensure you have Python 3.6 or higher installed on your system.

2. **Clone or Download**: Download the project files to your local machine.

3. **Run the Application**: Navigate to the project directory and run:
   ```bash
   python main.py
   ```

## Usage

### Starting the Application
Run the main script to start the application:
```bash
python main.py
```

### Main Menu Options
1. **Register** - Create a new user account
2. **Login** - Access existing account
3. **Exit** - Close the application

### Registration Process
When registering, you'll need to provide:
- First name
- Last name
- Email address (must be valid format)
- Password (with confirmation)
- Mobile phone number (Egyptian format: 01XXXXXXXXX)

### Project Menu (After Login)
Once logged in, you can access the following options:
1. **Create Project** - Start a new crowd-funding campaign
2. **View All Projects** - Browse all projects in the system
3. **Edit My Project** - Modify your existing projects
4. **Delete My Project** - Remove your projects
5. **Search Projects by Date** - Find projects active on specific dates
6. **Logout** - Return to main menu

### Creating a Project
When creating a project, you'll need to provide:
- **Title**: Project name
- **Details**: Project description
- **Total Target**: Funding goal in EGP
- **Start Date**: Campaign start date (YYYY-MM-DD format)
- **End Date**: Campaign end date (YYYY-MM-DD format)

## Data Storage

The application uses JSON files for data persistence:
- `users.json`: Stores user account information
- `projects.json`: Stores project data

## Technical Details

### Dependencies
- **Python Standard Library**: No external dependencies required
- **JSON**: For data storage
- **Regular Expressions**: For input validation
- **Datetime**: For date handling and validation

### Validation Rules
- **Email**: Must follow standard email format (user@domain.com)
- **Phone**: Must be Egyptian mobile format (01XXXXXXXXX)
- **Dates**: Must be in YYYY-MM-DD format and end date must be after start date
- **Target Amount**: Must be a valid number

### Security Features
- Password confirmation during registration
- User authentication for project management
- Owner-only access for project editing and deletion

## Error Handling

The application includes comprehensive error handling for:
- Invalid input formats
- Duplicate email registration
- Authentication failures
- Invalid date ranges
- File I/O operations