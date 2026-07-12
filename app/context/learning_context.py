current_subject = None
current_topic = None
current_session = None


def set_current_subject(subject):
    global current_subject
    current_subject = subject


def get_current_subject():
    return current_subject


def set_current_topic(topic):
    global current_topic
    current_topic = topic


def get_current_topic():
    return current_topic


def set_current_session(session):
    global current_session
    current_session = session


def get_current_session():
    return current_session