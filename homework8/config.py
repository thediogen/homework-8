import os

from dotenv import load_dotenv


load_dotenv(override=True)

secret_app_key = os.getenv('secret_key')
