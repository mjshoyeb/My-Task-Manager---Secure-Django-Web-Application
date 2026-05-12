**My Task Manager - Secure Django Web Application**

    A robust, multi-user Task Management system built using the Django web framework. This project demonstrates the implementation of secure user authentication, database relationship management, and a modern, responsive front-end experience.

**🚀 Overview**
    The primary goal of this project was to create a personalized productivity tool where users can manage their daily tasks in a secure environment. Unlike basic To-Do apps, this application implements strict data isolation, ensuring that every user has a private dashboard.

**✨ Core Functionalities**
    * User Authentication: Secure signup, login, and logout flow using Django’s built-in authentication system.

    * Data Ownership: Implemented using a ForeignKey relationship, ensuring users can only access their own records.

    * Dynamic Task Management: Full CRUD (Create, Read, Update, Delete) capabilities with real-time status updates.

    * Advanced Search & Filter: Efficiently query tasks using a built-in search bar.

    * State Persistence: Integrated "Mark as Complete" logic with visual feedback (strikethrough and color coding).

    * Browser Interaction: Custom JavaScript implementation for dynamic tab titles based on the user's task count and window focus.

**🛠 Technical Implementation**
    -> Backend: Python 3.12, Django 5.0.x

    -> Database: SQLite3 (Development standard)

    -> Frontend: HTML5, CSS3 (Custom Geometric Patterns), Bootstrap 5.3

    -> Architecture: Model-View-Template (MVT)

**⚙️ Local Development Setup**
To get this project running on your local machine or in a lab environment:

* Clone the repository:

Bash
    git clone <your-repository-url>
    cd MyWebProject

* Environment Setup:
(It is recommended to use a virtual environment.)

Bash
    python -m venv venv
    source venv/bin/Scripts/activate  # On Windows: venv\Scripts\activate

* Install Dependencies:

    Bash
    pip install -r requirements.txt

* Apply Migrations:

    Bash
    python manage.py migrate

* Start the Server:

    Bash
    python manage.py runserver

* Access the application at http://127.0.0.1:8000/.

**📂 Project Structure**

    my_site/ - Core project configuration and settings.

    todo_app/ - Application logic including models for task handling and user-specific views.

    templates/ - Modular HTML structure with template inheritance.

    static/ - Managed assets including custom CSS, geometric background patterns, and favicons.

**📝 Key Learning Outcomes**
    During the development of this project, I focused on:
    - Implementing Class-Based Views (CBV) for authentication and Function-Based Views (FBV) for task logic.

    - Handling Django's security requirements for POST requests (CSRF protection and Logout methods).

    - Frontend optimization using Glassmorphism and CSS Grid/Flexbox.

------------------------------------------------------------------
Developed by: MJ Shoyeb
Roll/ID: 2285055
Institution: A K Khan UCEP Polytechnic Institute (AKKUPI)