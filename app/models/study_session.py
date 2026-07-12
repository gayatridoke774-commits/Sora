from dataclasses import dataclass
from datetime import datetime


@dataclass
class StudySession:
    session_id: str
    user_id: str
    subject_id: str
    subject_name: str
    topic_id: str
    topic_name: str
    start_time: datetime
    end_time: datetime
    duration_minutes: float
    created_at: datetime

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "user_id": self.user_id,
            "subject_id": self.subject_id,
            "subject_name": self.subject_name,
            "topic_id": self.topic_id,
            "topic_name": self.topic_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "duration_minutes": self.duration_minutes,
            "created_at": self.created_at,
        }