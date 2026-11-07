# DTI412 - Lab Assignment 2: CoursePortal

Django Core Architecture, MVT Pattern & Dynamic Request Handling

### Project Overview
`CoursePortal` is an interactive Course Catalog and Student Inquiry web application built with Django 5.x and Bootstrap 5 for the IT department.

### Features
- **MVT Architecture:** Clean separation of concerns between Models, Views, and Templates.
- **Dynamic Routing:** URL dispatcher with parameter passing (`/courses/<int:course_id>/`).
- **Bootstrap 5 Integration:** Responsive UI with cards, badges, navbar, and grid system.
- **Form Processing & CSRF Protection:** Server-side input validation and Cross-Site Request Forgery security tokens.
- **Extension Challenge:** Live course search filtering by course code and title via GET parameter (`/courses/?q=...`).

### Application Routes
- `/` - Homepage with portal metrics (total active courses, featured course).
- `/courses/` - Full catalog of offered IT courses with search filter.
- `/courses/<int:course_id>/` - Dynamic course syllabus details (e.g. `/courses/101/`).
- `/inquiry/` - Student course inquiry form with server-side validation and feedback.

### Quick Start Instructions

1. **Activate Virtual Environment:**
   - On Windows (PowerShell):
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```cmd
     .\venv\Scripts\activate.bat
     ```

2. **Navigate to the Project Directory:**
   ```powershell
   cd courseportal
   ```

3. **Run Migrations (Initial Setup):**
   ```powershell
   python manage.py migrate
   ```

4. **Run the Development Server:**
   ```powershell
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

5. **Run Automated Test Suite:**
   ```powershell
   python manage.py test
   ```

---

### Student Information
- **Course:** DTI412 Special Topic in Application Development
- **GitHub:** [RexX0Dora1005](https://github.com/RexX0Dora1005)
