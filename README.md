# Invoice Management System

The Invoice Management System is a web-based application designed to streamline the process of creating, managing, and tracking invoices. It helps businesses maintain accurate records of their transactions, customers, and payments with an intuitive and user-friendly interface.

# 🚀 Features

Create, update, and delete invoices

Manage customer details

Track invoice payment status (Paid / Pending)

View list of all invoices and customers

Search and filter invoices

Download invoices as PDF (optional feature)

Admin authentication and authorization (optional feature)

# 🛠️ Tech Stack

Backend: Python, Django / FastAPI (based on your project)

Frontend: HTML, CSS, JavaScript (optionally Bootstrap for design)

Database: MySQL / SQLite

Other Tools:

Django REST Framework (if APIs are used)

ReportLab / WeasyPrint (for PDF generation)

Postman (for API testing)

# 🏗️ Project Structure

invoice-management-system/

├── backend/

│   ├── manage.py

│   ├── invoice_app/

│   │   ├── models.py

│   │   ├── views.py

│   │   ├── urls.py

│   │   ├── serializers.py (if APIs are used)

│   │   ├── templates/

│   │   └── static/

│   └── settings.py

├── README.md

├── requirements.txt

└── database/

    └── db.sqlite3 


# ⚙️ Installation and Setup

1. Clone the repository

    git clone https://github.com/shashanksaranr/invoice-management-system.git

    cd invoice-management-system

2. Create a virtual environment

    python -m venv venv

    source venv/bin/activate   # For Linux/Mac

    venv\Scripts\activate      # For Windows

3. Install dependencies
   
    pip install -r requirements.txt

4. Apply migrations
   
    python manage.py makemigrations

    python manage.py migrate

5. Run the server
   
    python manage.py runserver

6. Access the application
   
    Open http://127.0.0.1:8000 in your browser.

8. Testing

    python manage.py test


🙋‍♂️ Author

SHASHANKSARAN R

GitHub: @shashanksaranr

