---

# **To-Do List Application**

A simple and elegant to-do list application built using Django. This app allows users to manage their tasks efficiently by adding and viewing them.

---

## **Features**
- Add new tasks.
- View a list of tasks.
- Simple, responsive, and modern UI.

---

## **Tech Stack**
- **Backend:** Django 5.0.3
- **Frontend:** HTML, CSS (with optional Bootstrap)
- **Database:** SQLite (default Django database)

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.11 or higher installed on your system.
- `pip` package manager.

### **Steps to Run the Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/SeeminKhan/Spacece-Task.git
   cd Spacece-Task
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:
   - Navigate to `http://127.0.0.1:8000/`.

---

## **Project Structure**
```
todo_project/
├── todo/
│   ├── migrations/
│   ├── static/
│   │   ├── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── view_tasks.html
│   │   ├── add_task.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── manage.py
├── requirements.txt
```
