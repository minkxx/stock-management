import os
from dotenv import load_dotenv

from management.database import Database

load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
RUN_MODE = int(os.getenv("RUN_MODE"))


database = Database(uri=MONGO_DB_URI, db_name="stock-management")
