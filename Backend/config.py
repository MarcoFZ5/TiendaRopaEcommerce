import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    SERVER = os.getenv("DB_SERVER")
    DATABASE = os.getenv("DB_DATABASE")
    DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")
    TRUST_CERT = os.getenv("DB_TRUST_CERT", "yes")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}/{DATABASE}"
        f"?driver={DRIVER}&TrustServerCertificate={TRUST_CERT}"
    )