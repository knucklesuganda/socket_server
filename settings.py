import os
from dotenv import load_dotenv

load_dotenv('.env')

ENCODING = os.environ['ENCODING']
SERVER_ADDRESS = (os.environ['SERVER_HOST'], int(os.environ['SERVER_PORT']))
ENCRYPTION_KEY = int(os.environ['ENCRYPTION_KEY'])
