import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SERVER = os.getenv("DB_SERVER")
    DATABASE = os.getenv("DB_DATABASE")
    DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
    TRUST_CERT = os.getenv("DB_TRUST_CERT", "yes")
    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://@{SERVER}/{DATABASE}"
        f"?driver={DRIVER}&TrustServerCertificate={TRUST_CERT}&trusted_connection=yes"
    )