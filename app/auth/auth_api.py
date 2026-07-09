from urllib import response

import requests

from app.config.settings import FIREBASE_API_KEY

SIGNUP_URL = (
    "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
)

def signup(email: str, password: str):
                payload = {
                        "email":email,
                        "password":password,
                        "returnSecureToken":True
                }

                response = requests.post(
                 SIGNUP_URL,
                 params={"key": FIREBASE_API_KEY},
                 json=payload
               )

                return response.json()

def login(email: str, password: str):
    url = (
        f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        f"?key={FIREBASE_API_KEY}"
    )

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=payload)

    return response.json()