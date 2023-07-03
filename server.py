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


ENVIRONMENT : str = "PRODUCTION"
config = DevelopmentEnvironment()

match ENVIRONMENT.upper():
    case "PRODUCTION":
        config = ProductionEnvironment()
    
    case "TESTING":
        config = TestingEnvironment()

    case _:
        config = DevelopmentEnvironment()


app : Flask = create_bookstore_app(config)

if __name__ == "__main__":

    match ENVIRONMENT.upper():
        case "PRODUCTION" : 
            app.run()

        case _:
            app.run(debug=True, host="0.0.0.0", port="5000")