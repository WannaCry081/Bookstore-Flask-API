from App import create_bookstore_app
from flask import Flask


app : Flask = create_bookstore_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    # app.run()