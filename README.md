# 📚 EtLib – Ethiopian Digital Library API

EtLib is a RESTful API built with **Django REST Framework** and **MySQL**, designed to serve as a digital library system for Ethiopian institutions, schools, and communities.  
It allows **librarians** to manage book inventories and **users** to borrow and return books.  
The goal is to improve access to books and learning materials digitally.

---

## 🌐 Live Demo

- 🔗 [Backend API]("Coming soon")

---

## 🧰 Tech Stack

- Django + Django REST Framework
- MySQL (Relational Database)
- JWT Authentication (`djangorestframework-simplejwt`)
- RESTful API

---

## 📂 Project Structure

```
etlib/
├── books/               # Book management (CRUD + Borrow/Return)
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/               # User management + authentication
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── etlib/               # Main Django configuration
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Eyobed9/EtLib.git

# Navigate to the project directory
cd EtLib

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your browser or test endpoints in **Postman**.

---

## 🔐 Environment Variables

Create a `.env` file and configure your database + secret key:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=etlib_db
DB_USER=etlib_user
DB_PASSWORD=abc123
DB_HOST=localhost
DB_PORT=3306
```

---

## 🧪 Testing with Postman

- ✅ Register → Login → Get JWT token  
- ✅ Add Book (Librarian only)  
- ✅ List/Search Books (All users)  
- ✅ Checkout Book → Borrow record created  
- ✅ Return Book → Copies updated  
- ✅ View “My Borrowed Books” history  

---

## 🚀 Features (MVP – 5 Days)

- 🔐 User Authentication (Register/Login with JWT)
- 👥 Roles: Librarians vs Users
- 📚 Book Management (CRUD with permissions)
- 📦 Borrowing System (Checkout & Return)
- 📖 Borrow History (My Books + All records for librarians)

---

## 📸 Screenshots (Optional)

| Admin Panel                       | API in Postman                       |
| --------------------------------- | ------------------------------------ |
| ![Admin](./screenshots/admin.png) | ![Postman](./screenshots/postman.png) |

---

## 🛡️ License

This project is licensed under the [MIT License](./LICENSE).

---

## 👏 Contributing

Contributions are welcome! Please fork the repo and open a pull request.

```bash
git clone https://github.com/Eyobed9/EtLib.git
git checkout -b feature/feature-name
```

---

## 📬 Contact

For questions, reach out at **[eyobedteshome@gmail.com](mailto:eyobedteshome@gmail.com)**  
or connect via [LinkedIn](https://www.linkedin.com/in/eyobed-d-249634230/).

---

## 🙏 Acknowledgments

- [Django](https://docs.djangoproject.com/en/5.2/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
