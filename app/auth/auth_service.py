from datetime import datetime

from app.auth.auth_api import signup
from app.models.user import User
from app.services.user_service import create_user

from app.auth.auth_api import login
from app.session.session_manager import save_session

from app.services.user_service import get_user
from app.session.current_user import set_current_user

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

def login_user(email: str, password: str):
    response = login(email, password)

    if "localId" not in response:
        return {
            "success": False,
            "message": response["error"]["message"]
        }

    user = get_user(response["localId"])

    if user is None:
        return {
            "success": False,
            "message": "User profile not found."
        }

    set_current_user(user)

    save_session(
        uid=user["uid"],
        name=user["name"],
        email=user["email"]
    )

    return {
        "success": True,
        "message": "Login successful!"
    }