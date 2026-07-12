from datetime import datetime
from app.config.firebase import db


def create_subject(subject):
    """Create a new subject for the current user."""

    db.collection("users") \
        .document(subject.user_id) \
        .collection("subjects") \
        .document(subject.subject_id) \
        .set(subject.to_dict())


def get_subjects(user_id):
    """Return all subjects belonging to a user."""

    docs = (
        db.collection("users")
        .document(user_id)
        .collection("subjects")
        .stream()
    )

    subjects = []

    for doc in docs:
        subjects.append(doc.to_dict())

    return subjects


def delete_subject(user_id, subject_id):
    """Delete a subject."""

    db.collection("users") \
        .document(user_id) \
        .collection("subjects") \
        .document(subject_id) \
        .delete()