import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AI_DEVS_SERVER = os.environ.get('AI_DEVS_SERVER')
AI_DEVS_API_KEY = os.environ.get('AI_DEVS_API_KEY')
OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')

qdrant_url = os.environ.get('QDRANT_URL')