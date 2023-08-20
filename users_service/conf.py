import os
import environ

environ.Env()
environ.Env.read_env()
    
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_SECRET_KEY = os.environ.get('GOOGLE_SECRET_KEY')