class Config:
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    SQL_ALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<password>@localhost:3306/<db_schema>'
