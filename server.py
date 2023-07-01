"""
Bookstore API 
Developed by Lirae Que Data
"""
from flask import Flask
from App import create_bookstore_app
from Config import (
    ProductionEnvironment, 
    DevelopmentEnvironment,
    TestingEnvironment
)


ENVIRONMENT : str = "DEVELOPMENT"
config = None

match ENVIRONMENT:
    case "DEVELOPMENT":
        config = DevelopmentEnvironment()
        
    case "PRODUCTION":
        config = ProductionEnvironment()
    
    case _:
        config = TestingEnvironment()


app : Flask = create_bookstore_app(config)

if __name__ == "__main__":

    # Development Environment
    # Uncomment the line below to enable debug mode and allow access from any host
    app.run(debug=True, host="0.0.0.0")

    # Production Environment
    # app.run()



    # Admin has the ID = 1