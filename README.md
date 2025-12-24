# STUDENT REGISTER SYSTEM
#### Video Demo: <url>
#### Description:

The Student Register System is a command-line application written in Python that allows users to manage student records efficiently. The system stores student information including student numbers, names, classrooms, and grades in a CSV file, providing persistent storage across sessions.

## Project Structure

The project consists of two main files:

### project.py
This is the main application file containing:
- **Student Class**: A class that represents individual students with attributes like student number, first name, last name, classroom, and grade
- **StudentRegister Class**: Manages the collection of students and handles file operations
- **Main Menu System**: Provides an interactive interface for users to perform various operations
- **Helper Functions**: Functions for adding, removing, searching, and listing students

### test_project.py
Contains unit tests using pytest to verify the functionality of key features:
- `test_add_student()`: Verifies that students can be added correctly
- `test_remove_student()`: Tests both successful and unsuccessful removal operations
- `test_search_student()`: Ensures the search functionality works properly

## Features

### 1. Add New Student
Users can register new students by providing:
- Student number (unique identifier)
- First name
- Last name
- Classroom
- Grade (optional)

The system validates that the student number doesn't already exist and ensures required fields are not empty.

### 2. Delete a Student
Allows removal of students by their student number. The system:
- Searches for the student first
- Shows student information for confirmation
- Asks for user confirmation before deletion
- Automatically saves changes to the CSV file

### 3. Search a Student
Users can search for specific students using their student number. The system displays all information about the found student in a formatted manner.

### 4. List All Students
Displays all registered students with:
- Total count of students
- Formatted list showing all student details
- Clear visual separation using dividers

### 5. Save and Exit
Saves all changes to the CSV file and exits the program.

## Design Decisions

### Why CSV Format?
I chose CSV (Comma-Separated Values) format for data storage because:
- It's simple and human-readable
- Easy to import/export to other applications like Excel
- Built-in Python support through the csv module
- Lightweight without requiring external databases

### Class-Based Architecture
I implemented two main classes (Student and StudentRegister) to:
- Separate concerns between individual student data and the collection management
- Make the code more maintainable and extensible
- Follow object-oriented programming principles taught in CS50

### Dictionary for Student Storage
I used a dictionary with student numbers as keys because:
- O(1) lookup time for searching students
- Prevents duplicate student numbers automatically
- Easy to check if a student exists before adding

### Automatic Saving
The system saves to file after every add/remove operation to prevent data loss, though this could be optimized for larger datasets by implementing a manual save option.

## How to Run

1. Ensure Python 3 is installed on your system
2. Run the program:
```
   python project.py
```
3. Follow the on-screen menu to manage student records

## Running Tests

To run the test suite:
```
pytest test_project.py -v
```
## Requirements

- Python 3.6 or higher
- pytest (for running tests)

---
This project was created as the final project for CS50's Introduction to Programming with Python.