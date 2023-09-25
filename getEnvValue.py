from dotenv import load_dotenv
import os


def getEnvValue(key):
  load_dotenv()
  return os.getenv(key)
