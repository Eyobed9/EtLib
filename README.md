# EtLib - Ethiopian digital library

EtLib is a RESTful API built with Django REST Framework and MySQL, designed to serve as a digital library system for Ethiopian institutions, schools, and communities. The API will allow librarians to manage book inventories and users to borrow and return books. The goal is to improve access to books and learning materials digitally

---

## 🌐 Live Demo

- 🔗 [Frontend Demo]("Comming soon")
- 🔗 [Backend API Docs]("Comming soon")

---

## 🧰 Tech Stack

- Django
- MySQL
- JWT Authentication / OAuth
- RESTful API / GraphQL

---

## 📂 Project Structure

etlib/
├── books/               # App for book-related logic
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── users/               # App for user-related logic
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── etlib/               # Main Django config
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/Eyobed9/EtLib.git

# Navigate to the project directory
cd EtLib

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) with your browser to see the result.

---

## 🔐 Environment Variables

Add the following to your `.env` files:

**Backend `.env`**

```
PORT=5000
DB_URI=mongodb://localhost:27017/myapp
JWT_SECRET=your_jwt_secret_key
```

---

## 🧪 Testing

```bash
# Run backend tests
cd server
npm test

```
---

## 🚀 Features

* 🔐 User Authentication (Login/Register/JWT)
* 📦 API with CRUD operations

---

## 📸 Screenshots

| Home Page                       | Admin Panel                       |
| ------------------------------- | --------------------------------- |
| ![Home](./screenshots/home.png) | ![Admin](./screenshots/admin.png) |

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

For questions, reach out at [eyobedteshome@gmail.com] → [eyobedteshome@gmail.com](mailto:eyobedteshome@gmail.com) or connect via [LinkedIn](https://www.linkedin.com/in/eyobed-d-249634230/).

---

## 🙏 Acknowledgments

* [Django](https://docs.djangoproject.com/en/5.2/)