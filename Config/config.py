from App.utils import keyGenerator
from datetime import timedelta


DB_NAME : str = "book_db"


class DevelopmentEnvironment:
    
    DEBUG : bool = True
    SECRET_KEY : str = keyGenerator(10)
    JWT_SECRET_KEY : str = keyGenerator(10)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    JWT_BLACKLIST_ENABLED : bool = True

    # SQLite3 Database
    SQLALCHEMY_DATABASE_URI : str = f"sqlite:///{DB_NAME}.sqlite3"
    
    JWT_ACCESS_TOKEN_EXPIRATIONS : timedelta = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRATIONS : timedelta = timedelta(days=30) 


class ProductionEnvironment:

    DEBUG : bool = False
    SECRET_KEY : str = keyGenerator(18)
    JWT_SECRET_KEY : str = keyGenerator(18)

    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False
    JWT_BLACKLIST_ENABLED : bool = True

    # MySQL Database
    SQLALCHEMY_DATABASE_URI : str = f"mysql://root:data@localhost:3306/{DB_NAME}"

    JWT_ACCESS_TOKEN_EXPIRATIONS : timedelta = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRATIONS : timedelta = timedelta(days=1) 


class TestingEnvironment:
    
    pass