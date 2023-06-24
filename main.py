"""
Bookstore API 
Developed by Lirae Que Data
"""

from App import create_bookstore_app
from flask import Flask


app : Flask = create_bookstore_app()

if __name__ == "__main__":

    # Development Environment
    # Uncomment the line below to enable debug mode and allow access from any host
    # app.run(debug=True, host="0.0.0.0")

    # Production Environment
    app.run()



    # Admin has the ID = 1