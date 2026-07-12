from app.config.firebase import db


def create_topic(topic):
    db.collection("users") \
        .document(topic.user_id) \
        .collection("subjects") \
        .document(topic.subject_id) \
        .collection("topics") \
        .document(topic.topic_id) \
        .set(topic.to_dict())


def get_topics(user_id, subject_id):
    docs = (
        db.collection("users")
        .document(user_id)
        .collection("subjects")
        .document(subject_id)
        .collection("topics")
        .stream()
    )

    topics = []

    for doc in docs:
        topics.append(doc.to_dict())

    return topics


def delete_topic(user_id, subject_id, topic_id):
    db.collection("users") \
        .document(user_id) \
        .collection("subjects") \
        .document(subject_id) \
        .collection("topics") \
        .document(topic_id) \
        .delete()