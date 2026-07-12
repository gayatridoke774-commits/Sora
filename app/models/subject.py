from dataclasses import dataclass
from datetime import datetime


@dataclass
class Subject:
    subject_id: str
    user_id: str
    name: str
    progress: float = 0.0
    total_topics: int = 0
    completed_topics: int = 0
    weak_topics: int = 0
    study_hours: float = 0.0
    priority: int = 3
    created_at: datetime = None
    last_studied: datetime = None

    def to_dict(self):
        return {
            "subject_id": self.subject_id,
            "user_id": self.user_id,
            "name": self.name,
            "progress": self.progress,
            "total_topics": self.total_topics,
            "completed_topics": self.completed_topics,
            "weak_topics": self.weak_topics,
            "study_hours": self.study_hours,
            "priority": self.priority,
            "created_at": self.created_at,
            "last_studied": self.last_studied,
        }