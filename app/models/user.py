from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    uid: str
    name: str
    email: str
    created_at: datetime
    last_active: datetime
    streak: int = 0
    total_study_hours: float = 0.0

    def to_dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
            "last_active": self.last_active,
            "streak": self.streak,
            "total_study_hours": self.total_study_hours,
        }