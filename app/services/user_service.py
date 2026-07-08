from app.config.firebase import db


def create_user(user):
    db.collection("users").document(user.uid).set(user.to_dict())