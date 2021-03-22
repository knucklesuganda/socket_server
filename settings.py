import os
from dotenv import load_dotenv

load_dotenv('.env')

ENCODING = os.environ['ENCODING']
SERVER_ADDRESS = os.environ['SERVER_ADDRESS']
ENCRYPTION_KEY = os.environ['ENCRYPTION_KEY']
