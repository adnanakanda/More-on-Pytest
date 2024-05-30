from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
BASE_API_URL = "https://api.spotify.com/v1"
TOKEN_URL = "https://accounts.spotify.com/api/token"

