from dotenv import load_dotenv
import os

load_dotenv()

sqlServerName = os.getenv("sqlServerName")
databaseName = os.getenv("databaseName")
trusted_connection = os.getenv("trusted_connection")

connection_string = (
    f"DRIVER={{SQL Server}};"
    f"SERVER={sqlServerName};"
    f"DATABASE={databaseName};"
    f"Trusted_Connection={trusted_connection}"
)