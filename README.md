# Student Profile Management System

A Django-based web application for managing student profiles with features to add, view, and manage student information including profile images.

## 📋 Project Overview

This is a third assessment project built with Django that provides a complete student profile management system. Users can create student records, upload profile images, view lists of all students, and access detailed student information.

## 🚀 Features

- **Add Students**: Create new student profiles with name, email, age, and profile image
- **Student List**: View all registered students with their information
- **Student Details**: View detailed information about individual students
- **Profile Images**: Upload and manage student profile pictures
- **Email Validation**: Ensure unique email addresses for each student
- **AJAX Integration**: Smooth form submission without page reload
- **Responsive Design**: Clean, user-friendly interface with Bootstrap styling

## 📁 Project Structure

```
student_profile_main/
├── app_student_info/              # Main application
│   ├── models.py                  # Database models (Student)
│   ├── views.py                   # View logic for handling requests
│   ├── urls.py                    # URL routing configuration
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # App configuration
│   ├── migrations/                # Database migrations
│   └── __pycache__/               # Python cache files
├── student_profile_main/          # Project configuration
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   ├── asgi.py                    # ASGI configuration
│   └── views.py                   # Project-level views
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── include/
│   │   └── navbar.html            # Navigation bar
│   └── student/
│       ├── add_student.html       # Add student form
│       ├── student_list.html      # List all students
│       └── details.html           # Student details page
├── static/                        # Static files
│   └── profile_ajax.js            # AJAX functionality
├── media/
│   └── profiles/                  # Student profile images
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django management script
└── README.md                      # This file
```

## 🛠️ Technology Stack

- **Backend**: Django 5.2
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Images**: Pillow (for image handling)
- **AJAX**: JavaScript with JSON responses

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or Navigate to the Project**
   ```bash
   cd student_profile_main
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django pillow
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main Application: `http://localhost:8000/student/list/`
   - Admin Panel: `http://localhost:8000/admin/`

## 📝 Usage

### Adding a Student
1. Navigate to the "Add Student" page
2. Fill in the form with:
   - Student Name (required)
   - Email (required, must be unique)
   - Age (required)
   - Profile Image (optional)
3. Click "Add Student"
4. You'll be redirected to the student list upon success

### Viewing Students
- Visit `/student/list/` to see all registered students
- Click on any student to view their detailed profile

### Viewing Student Details
- Click on a student's name from the list
- View complete student information and profile image

## 🗄️ Database Models

### Student Model
```python
class Student(models.Model):
    name = CharField(max_length=100)        # Student's full name
    email = EmailField(unique=True)         # Unique email address
    age = PositiveIntegerField()            # Student's age
    profile_image = ImageField()            # Student's profile picture
    created_at = DateTimeField()            # Timestamp of record creation
```

## 🔗 URL Routes

| Route | View | Purpose |
|-------|------|---------|
| `/student/add/` | add_student | Display add student form |
| `/student/list/` | student_list | Display all students |
| `/student/<id>/` | student_detail | View specific student details |

## 🔍 API Endpoints

### POST `/student/add/`
**Request**: Form data with student information
**Response**: JSON
```json
{
    "success": true,
    "message": "Student added successfully!",
    "redirect_url": "/student/list/"
}
```

## 🎨 Frontend Features

- **Responsive Navigation Bar**: Included navbar for easy navigation
- **Bootstrap Styling**: Clean and professional UI
- **AJAX Form Submission**: Smooth form submission without page reload
- **Form Validation**: Client and server-side validation
- **Profile Image Display**: Shows student profile pictures on list and detail pages

## ⚙️ Configuration

Key settings in `settings.py`:
- Debug mode: `True` (for development)
- Installed apps: Django default apps + `app_student_info`
- Database: SQLite (`db.sqlite3`)
- Media files: Served from `/media/` directory
- Static files: Served from `/static/` directory

## 🔐 Security Notes

- Change `SECRET_KEY` before production deployment
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` with your domain name
- Use environment variables for sensitive information
- Implement proper authentication and authorization

## 📝 License

This project is created as part of an assessment and is available for educational purposes.

## 👤 Author

Created by Rishikesh for Django Assessment Project

## 🤝 Support & Contributions

For issues or improvements, please review the code and make necessary modifications.

---

**Last Updated**: January 2026
