import os
from dotenv import load_dotenv
from datetime import datetime

from management.database import Database
from management.logger import Log

logger = Log(save_to_file=True)

logger.info("Setting environment varibale")
load_dotenv()

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
RUN_MODE = int(os.getenv("RUN_MODE"))

logger.info("Init database")

database = Database(uri=MONGO_DB_URI, db_name="stock-management")

collection = database.collection("store")
