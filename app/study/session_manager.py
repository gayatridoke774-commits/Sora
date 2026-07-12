from datetime import datetime
import uuid

from app.models.study_session import StudySession
from app.services.study_session_service import create_study_session
from app.context.learning_context import (
    set_current_session
)


class StudySessionManager:

    def start_session(self, user, subject, topic):

        # Record start time
        start_time = datetime.now()

        print("\n" + "=" * 40)
        print(f"📖 Studying: {topic['name']}")
        print("=" * 40)
        print(f"Started at: {start_time.strftime('%I:%M %p')}")
        print("\nGood luck with your study session!")
        input("\nPress ENTER when you finish studying...")

        # Record end time
        end_time = datetime.now()

        # Calculate duration in minutes
        duration = (end_time - start_time).total_seconds() / 60

        # Create study session object
        session = StudySession(
            session_id=str(uuid.uuid4()),
            user_id=user["uid"],
            subject_id=subject["subject_id"],
            subject_name=subject["name"],
            topic_id=topic["topic_id"],
            topic_name=topic["name"],
            start_time=start_time,
            end_time=end_time,
            duration_minutes=round(duration, 2),
            created_at=start_time
        )

        # Save current session in memory
        set_current_session(session)

        # Save session to Firestore
        create_study_session(session)

        # Clear current session
        set_current_session(None)

        print("\n" + "=" * 40)
        print("✅ Study Session Completed!")
        print("=" * 40)
        print(f"📘 Subject : {subject['name']}")
        print(f"📖 Topic   : {topic['name']}")
        print(f"⏱ Duration: {round(duration, 2)} minutes")
        print("💾 Session saved successfully!")
        print("=" * 40)