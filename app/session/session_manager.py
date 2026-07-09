import json
import os
from datetime import datetime

SESSION_FILE = "storage/session.json"


def save_session(uid, name, email):
    """Save the currently logged-in user."""

    os.makedirs("storage", exist_ok=True)

    session = {
        "uid": uid,
        "name": name,
        "email": email,
        "login_time": datetime.now().isoformat(),
        "last_subject": None,
        "last_topic": None
    }

    with open(SESSION_FILE, "w") as file:
        json.dump(session, file, indent=4)


def load_session():
    """Load the saved session if it exists."""
    if not os.path.exists(SESSION_FILE):
        return None

    with open(SESSION_FILE, "r") as file:
        return json.load(file)


def clear_session():
    """Remove the current session."""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)


def is_logged_in():
    """Return True if a valid session exists."""
    return os.path.exists(SESSION_FILE)