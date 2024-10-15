from secrets import *
from getpass import getpass
import os

OPENAI_API_KEY = Openai_key
OPENAI_API_KEY = getpass()
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
