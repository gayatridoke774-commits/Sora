from app.config.firebase import db


def create_user(user):
    db.collection("users").document(user.uid).set(user.to_dict())


def get_user(uid):
    doc = db.collection("users").document(uid).get()

    if doc.exists:
        return doc.to_dict()

    return None