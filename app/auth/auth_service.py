from datetime import datetime

from app.auth.auth_api import signup
from app.models.user import User
from app.services.user_service import create_user


def register_user(name: str, email: str, password: str):
    response = signup(email, password)

    if "localId" not in response:
        return {
            "success": False,
            "message": response["error"]["message"]
        }

    uid = response["localId"]

    user = User(
        uid=uid,
        name=name,
        email=email,
        created_at=datetime.now(),
        last_active=datetime.now()
    )

    create_user(user)

    return {
        "success": True,
        "message": "User registered successfully!",
        "uid": uid
    }