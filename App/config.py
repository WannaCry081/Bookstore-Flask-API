from App.utils.key_generator_util import keyGenerator
from datetime import timedelta


DB_NAME : str = "book_db"


class Config:

    SECRET_KEY : str = keyGenerator(15)
    JWT_SECRET_KEY : str = keyGenerator(15)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False

    # SQLite3 Database
    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}.sqlite3"
    
    # MySQL Database
    # Uncomment the line below to use MySQL Database
    # Change the <user> and <password> to your configuration
    # SQLALCHEMY_DATABASE_URI : str = f"mysql://<user>:<password>@localhost:3306/{DB_NAME}"

    JWT_EXPIRATION_DELTA : timedelta = timedelta(days=1)