from dotenv import load_dotenv
import os

load_dotenv()

# Environment variables
def get_env(key):
    return os.getenv(key)