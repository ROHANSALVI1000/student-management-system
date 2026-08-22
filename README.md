# student-management-system
A Python/Flask student management system

# Student Management System

A web-based school management application built with Python and Flask, using PostgreSQL as the database. The application provides separate functionalities for students, teachers, and the principal.

## Technologies Used

* Python
* Flask
* PostgreSQL
* Psycopg
* SQL
* HTML
* Jinja2

## Features

### Student

* View examination results
* View timetable

### Teacher

* Upload student examination results
* Add timetable information
* Access syllabus section

### Principal

* Password-protected principal section
* Add teachers
* Delete teachers
* Update teacher information
* View teacher salary status, salary, and subject

### Database

The application uses PostgreSQL to store and manage:

* Student examination results
* Timetable information
* Teacher information
* Teacher salary and status details

The application performs SQL operations such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE` through Psycopg.

## Project Structure

```text
student-management-system/
│
├── APP.py
├── templates/
│   ├── login.html
│   ├── student.html
│   ├── viewresults.html
│   ├── viewtimetable.html
│   ├── teacher.html
│   ├── uploadresult.html
│   ├── timetable.html
│   ├── syllabus.html
│   ├── password.html
│   ├── principal.html
│   ├── add.html
│   ├── del.html
│   ├── update.html
│   └── viewstatus.html
│
└── README.md
```

## What I Learned

While building this project, I practiced:

* Creating web applications using Flask
* Creating Flask routes
* Handling GET and POST requests
* Working with HTML forms
* Connecting Python with PostgreSQL using Psycopg
* Writing SQL queries
* Performing CRUD operations
* Passing database results to HTML templates
* Using Jinja2 with Flask
* Building different application flows for students, teachers, and principals

## Future Improvements

* Improve authentication and password security
* Add proper user accounts for students and teachers
* Add student and teacher registration
* Complete the syllabus section
* Complete the parent section
* Improve error handling and validation
* Improve the user interface
* Move database credentials to environment variables
* Add more database relationships and functionality

## Project Status

This is a learning project that I built while learning Python, Flask, SQL, and PostgreSQL. I plan to continue improving it as I learn more about backend development and databases.

