# from dotenv import load_dotenv
# import os

# load_dotenv()

# print(os.getenv("GREETING"))

from dotenv import dotenv_values

config = dotenv_values(".env")

print(config["GREETING"])