from dataclasses import dataclass
from datetime import datetime


@dataclass
class Topic:
    topic_id: str
    subject_id: str
    user_id: str
    name: str

    is_completed: bool = False
    mandatory_assessment_completed: bool = False

    confidence: int = 0
    mistake_count: int = 0

    flashcard_count: int = 0
    question_count: int = 0

    created_at: datetime = None
    last_studied: datetime = None

    def to_dict(self):
        return {
            "topic_id": self.topic_id,
            "subject_id": self.subject_id,
            "user_id": self.user_id,
            "name": self.name,
            "is_completed": self.is_completed,
            "mandatory_assessment_completed": self.mandatory_assessment_completed,
            "confidence": self.confidence,
            "mistake_count": self.mistake_count,
            "flashcard_count": self.flashcard_count,
            "question_count": self.question_count,
            "created_at": self.created_at,
            "last_studied": self.last_studied,
        }