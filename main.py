from dotenv import load_dotenv
import os

# OPENAI_API_KEY = Openai_key
# OPENAI_API_KEY = getpass()
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv('API_SECRET')

print('API_KEY: ', api_key)
print("API_SECRET: ", api_secret)
