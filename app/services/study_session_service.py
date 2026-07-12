from app.config.firebase import db


def create_study_session(session):
    db.collection("users") \
        .document(session.user_id) \
        .collection("study_sessions") \
        .document(session.session_id) \
        .set(session.to_dict())


def get_user_sessions(user_id):
    docs = (
        db.collection("users")
        .document(user_id)
        .collection("study_sessions")
        .stream()
    )

    sessions = []

    for doc in docs:
        sessions.append(doc.to_dict())

    return sessions


def get_topic_sessions(user_id, topic_id):
    docs = (
        db.collection("users")
        .document(user_id)
        .collection("study_sessions")
        .where("topic_id", "==", topic_id)
        .stream()
    )

    sessions = []

    for doc in docs:
        sessions.append(doc.to_dict())

    return sessions