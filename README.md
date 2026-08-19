# Sticky Notes App

A simple Django web application for creating, viewing, updating, and deleting sticky notes.

## Project Overview

This project allows a user to:
- view all notes in a list
- open an individual note
- create a new note
- edit an existing note
- delete a note

The app uses Django's model-view-template architecture and stores notes in a SQLite database.

## Features

- CRUD functionality for notes
- Clean Django form-based creation and editing
- List and detail views for notes
- Database-backed storage
- Basic styling for a simple user interface

## Tech Stack

- Python 3.12
- Django 4.2
- SQLite

## Project Structure

```text
sticky_notes/
├── manage.py
├── requirements.txt
├── README.md
├── sticky_github.txt
├── notes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── static/
│   └── templates/
├── sticky_notes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── .venv/  (local environment, not usually committed)
```

## Setup Instructions

1. Open the project folder:

```bash
cd sticky_notes
```

2. Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Open the app in a browser:

```text
http://127.0.0.1:8000/
```

## Running Tests

```bash
python manage.py test
```

## Notes

- Keep the virtual environment local and do not commit it to version control.
- Generated database files such as `db.sqlite3` should also be excluded from source control when required.
- The app is designed to demonstrate a simple Django CRUD workflow and can be expanded with more features if needed.

## GitHub Repository

The project repository is linked in the file `sticky_github.txt`.
