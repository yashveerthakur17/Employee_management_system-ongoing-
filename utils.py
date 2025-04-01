import dotenv
import os
host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")
port = os.getenv("PORT", "3306")