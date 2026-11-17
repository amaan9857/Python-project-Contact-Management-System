# Contact Management System

## 1. Project Overview

The Contact Management System is a simple web-based application developed using Python and Streamlit. It helps users manage their contacts easily by adding, viewing, searching, updating, and deleting contact details.

The application stores contact information in a JSON file, so the data remains saved even after closing the application.

## 2. Technologies Used

- **Python:** Main programming language.
- **Streamlit:** Used to create the web application interface.
- **JSON:** Used to store contact information.
- **OS Module:** Used to check whether the contact file exists.

## 3. Features

1. **Add Contact:** Add a new contact with name, phone number, and email.
2. **View Contacts:** Display all saved contacts.
3. **Search Contact:** Search for a contact using their name.
4. **Update Contact:** Modify the phone number and email of an existing contact.
5. **Delete Contact:** Remove an existing contact from the system.

## 4. Project Structure

```text
Contact_Management_System/
│
├── app.py
├── contacts.json
└── README.md
```

- `app.py` – Main Python application.
- `contacts.json` – Stores contact details.
- `README.md` – Project documentation.

## 5. Installation

First, install Python on your computer.

Install the required Streamlit library using:

```bash
pip install streamlit
```

The JSON and OS modules are already available in Python. No separate installation is required.

## 6. How to Run the Project

**Step 1:** Open the project folder in VS Code.

**Step 2:** Open the terminal.

**Step 3:** Run the following command:

```bash
streamlit run app.py
```

**Step 4:** The application will open in your web browser.

**Step 5:** Select an operation from the sidebar to manage contacts.

## 7. Concepts Used

- Dictionaries
- Functions
- Conditional Statements
- File Handling
- JSON Data Storage
- Streamlit Widgets
- CRUD Operations

## 8. CRUD Operations

CRUD represents four basic operations:

| Operation | Description |
|---|---|
| Create | Add a new contact |
| Read | View and search contacts |
| Update | Modify existing contact details |
| Delete | Remove a contact |

## 9. Advantages

- Simple and user-friendly interface.
- Easy contact management.
- Saves data using JSON files.
- Reduces manual work.
- Easy to understand and use.

## 10. Conclusion

The Contact Management System is a beginner-friendly Python project that demonstrates the practical use of Python programming, dictionaries, functions, file handling, JSON, and Streamlit.

It provides an easy way to store and manage contact information through a simple web interface.
