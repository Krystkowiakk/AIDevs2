import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AI_DEVS_SERVER = os.environ.get('AI_DEVS_SERVER')
AI_DEVS_API_KEY = os.environ.get('AI_DEVS_API_KEY')
OPEN_AI_API_KEY = os.environ.get('OPEN_AI_API_KEY')
RENDER_FORM_API_KEY = os.environ.get('RENDER_FORM_API_KEY')
SERP_API_KEY = '36d8cd99f841a2b7c8aabaf9f7799fe7f32742b28755d51889812b19511420eb'

qdrant_url = os.environ.get('QDRANT_URL')