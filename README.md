# Blog Project

A simple Django-based blog project that allows users to create an account, login, create blog posts, and update their profiles.

## Features

- User authentication (signup, login, logout)
- Create, read, update, and delete blog posts
- User profile management
- Responsive UI with Tailwind CSS

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS, Tailwind CSS
- **Database**: SQLite (for development)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django installed: `pip install django`
- Tailwind CSS installed

## Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/blog_project.git
cd blog_project
2. Create a virtual environment and activate it
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run migrations
bash
Copy code
python manage.py migrate
5. Create a superuser
bash
Copy code
python manage.py createsuperuser
6. Run the development server
bash
Copy code
python manage.py runserver
7. Access the application
Visit http://127.0.0.1:8000/ in your browser to use the application.

Usage
Sign Up: Create a new account.
Login: Log in to access the dashboard and start creating blog posts.
Create Blog Post: Write and publish blog posts.
Profile Management: Update your profile information.
Project Structure
bash
Copy code
blog_project/
│
├── blog/                       # App for handling blog posts
│   ├── migrations/             # Database migrations
│   ├── templates/              # HTML templates
│   ├── static/                 # Static files (CSS, JS)
│   └── ...
├── blog_project/               # Project settings
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django management script
├── README.md                   # This file
└── requirements.txt            # Python dependencies
