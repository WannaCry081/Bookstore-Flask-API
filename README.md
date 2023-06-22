# Bookstore API

This is a RESTful API for managing a virtual bookstore. It allows users to perform various operations related to books, including retrieving book information, adding new books, updating book details, and deleting books.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- SQLite/MySQL

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sansqed/project-ceboom.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Bookstore-Flask-API
   ```

3. Create a virtual environment:

   ```bash
   virtualenv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source env/bin/activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:

   ```bash
   python main.py
   ```

2. The API endpoints can be accessed at `http://localhost:5000`. The available endpoints are:

   - `GET /books`: Retrieve all books.
   - `GET /books/<book_id>`: Retrieve details of a specific book.
   - `POST /books`: Add a new book.
   - `PUT /books/<book_id>`: Update details of a specific book.
   - `DELETE /books/<book_id>`: Delete a specific book.

3. You can use tools like cURL or Postman to interact with the API endpoints.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.
