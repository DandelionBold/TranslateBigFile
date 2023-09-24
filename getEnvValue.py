from dotenv import load_dotenv
import os


def get_env_value(key):
  load_dotenv()
  return os.getenv(key)
