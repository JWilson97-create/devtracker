# 📝 Flask Job Tracker

A lightweight Flask web application to track job applications. Built with Flask, SQLAlchemy, and SQLite.

---

## 🚀 Features

- Add new job applications (company, position, salary, status, etc.)
- View all jobs as JSON
- RESTful API with endpoints for:
  - `GET /jobs` — list all jobs
  - `POST /jobs` — add a new job

---

## 📁 Project Structure

devtracker/
├── app/
│ ├── init.py # Create Flask app
│ ├── routes.py # Job routes (GET, POST)
│ ├── models.py # SQLAlchemy models
│ └── database.py # Database config/setup
├── run.py # App entry point
├── requirements.txt # Dependencies
├── .gitignore # Ignored files/folders
└── README.md # Project info

