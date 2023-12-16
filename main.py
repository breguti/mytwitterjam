from dotenv import load_dotenv
import os
import base64

load_dotenv() #loads environment var by reading from a .env file

client_id = os.getenv("CLIENT_ID") #returns value of enviroment variable 
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret 
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_base64), "utf-8")