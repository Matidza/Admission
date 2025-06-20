# 🎓 Admissions - School Admission System

An online school admission platform built with Django and PostgreSQL that enables parents to apply for school admissions for their children from the comfort of their homes. This system provides a seamless and efficient way for parents to fill out application forms, submit required documents, and track the status of their child’s application.

📋 **Features**

- **Parent Authentication**:
  - Secure login and registration.
  - Parent profiles with personal details and application history.
  
- **Student Application Forms**:
  - Online forms for parents to submit their child's application.
  - Dynamic fields based on school criteria (age, grade, etc.).
  
- **Document Upload**:
  - Upload supporting documents such as birth certificates, previous school reports, and medical records.
  
- **Application Status Tracking**:
  - Real-time tracking of application status (Pending, Approved, Rejected).
  
- **Admin Dashboard**:
  - Admin interface to review and manage applications.
  - Review student details, documents, and make admission decisions.

- **Email Notifications**:
  - Automated email alerts sent to parents regarding application updates and required actions.

- **Multi-School Support**:
  - Support for multiple schools, each with different admission criteria.

- **Mobile-Friendly UI**:
  - Fully responsive design for a smooth experience on all devices.

🚀 **Getting Started**

### Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Django 4.x
- PostgreSQL (or another database of your choice)
- Virtualenv (recommended for setting up a virtual environment)

### Installation Steps



1. **Clone the Repository**

   Clone the repository to your local machine:
   
   ```bash
   git clone https://github.com/your-username/admissions.git
   cd admissions
   ```

2. **Create a Virtual Environment** (optional but recommended)

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use env\Scripts\activate
   ```

3. **Install Dependencies**

   Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL Database**

   Create a new PostgreSQL database and user. Then, update the database credentials in `settings.py`:
   
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run Migrations**

   Set up the database schema:
   
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (optional, for admin access)

   Create a superuser to access the admin panel:
   
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**

   Run the development server:
   
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to access the website.

🔗 **Integrating Email Notifications**

To send email notifications (for example, when the application status changes), configure email settings in `settings.py` with your email service provider credentials (e.g., Gmail, SendGrid, etc.).

For Gmail, add the following to `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

You can then use Django's `send_mail` function to send application status updates.

🧑‍💻 **Project Structure**

```
admissions/
│
├── manage.py               # Django management script
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables
├── db.sqlite3              # Local development database (if using SQLite)
│
├── admissions/             # Main Django app
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, Images
│   ├── models.py           # Database models
│   ├── views.py            # Views logic
│   ├── forms.py            # Forms for student application
│   └── urls.py             # URL routing
│
└── README.md               # Project documentation
```

🛠️ **Technologies Used**

- **Backend**: Django, Python
- **Database**: PostgreSQL (or SQLite for development)
- **Frontend**: HTML, CSS, Bootstrap
- **Email Notifications**: SMTP / SendGrid / Gmail
- **Forms**: Django Forms
- **Authentication**: Django User Authentication System

🐛 **Troubleshooting**

- **Database Connection Error**:
  Ensure PostgreSQL is installed and your credentials in `settings.py` are correct.
  
- **Missing Dependencies**:
  Run `pip install -r requirements.txt` if any dependencies are missing.
  
- **Email Configuration**:
  Double-check your email settings and ensure your credentials are correct.

🙌 **Contributing**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

📧 Email: admission.django@gmail.com
