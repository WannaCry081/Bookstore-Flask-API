# Bookstore API

Welcome to the Virtual Bookstore API, a robust and user-friendly solution for managing your online bookstore. Built with Flask, Flask-SQLAlchemy, Flask-Restful, Flask-Marshmallow, Flask-Bcrypt, Flask-Cors and Flask-JWT-Extended, this RESTful API seamlessly integrates with SQLite and MySQL databases, providing a versatile and scalable platform. With features like book retrieval, addition, update, deletion, user authentication, and admin privileges, the Virtual Bookstore API empowers you to efficiently manage your inventory. Experience the power and flexibility of the Virtual Bookstore API today and create an exceptional online bookstore experience.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite (for local development)
- MySQL (for production)

## Installation

1. Clone the repository:

```
git clone https://github.com/sansqed/project-ceboom.git
cd bookstore-flask-api
```

2. Create a virtual environment:

```
virtualenv env
```

3. Activate the virtual environment:

- For Linux/Mac:

```
source env/bin/activate
```

- For Windows:

```
env\Scripts\activate
```

4. Install the dependencies:

```
pip install -r requirements.txt
```

5. Run the application:

```
python manage.py runserver
```

The default database used in this project is SQLite3. However, you can also use it in MySQL by configuring the `config.py` in the `App/config.py` directory. Moreover, the API should now be accessible at `http://localhost:5000`.


## API Routes

- **POST /api/auth/signin/**
  - User sign-in with email and password.
  - Returns a JWT token for authentication.

- **POST /api/auth/signup/**
  - User sign-up with username, email, and password.
  - Creates a new user in the database.

- **POST /api/auth/signout/**
  - User sign-out.
  - Invalidates the JWT token.

- **GET /api/book/**
  - Get a list of all books.
  - No authentication required.

- **GET /api/book/<book_id>/<book_title>/**
  - Get details of a specific book.
  - No authentication required.

- **GET /api/book/booklist/**
  - Get the authenticated user's book list.

- **POST /api/book/booklist/**
  - Add a book to the authenticated user's book list.

- **DELETE /api/book/<book_id>/<book_title>/**
  - Delete a book from the authenticated user's book list.

- **GET /api/user/**
  - Get the authenticated user's profile.

- **PUT /api/user/**
  - Update the authenticated user's profile.

- **POST /api/user/**
  - Update the authenticated user's password.

- **DELETE /api/user/**
  - Delete the authenticated user's account.

- **POST /api/admin/book/**
  - Add a book (admin only).

- **PUT /api/admin/book/<book_id>/<book_title>/**
  - Update a book (admin only).

- **DELETE /api/admin/book/<book_id>/<book_title>/**
  - Delete a book (admin only).

- **GET /api/admin/user/**
  - Get a list of all users (admin only).

- **DELETE /api/admin/user/<user_id>/<username>/<email>/**
  - Delete a user (admin only).

## Contributing

Contributions to the project are welcome. If you find any issues or have any suggestions for improvement, feel free to submit a pull request or open an issue on the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

