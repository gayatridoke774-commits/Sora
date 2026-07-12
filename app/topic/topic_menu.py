import uuid
from datetime import datetime

from app.study.session_manager import StudySessionManager

from app.models.topic import Topic
from app.services.topic_service import (
    create_topic,
    get_topics,
    delete_topic
)


def topic_menu(subject, user):

    while True:

        print("\n" + "=" * 40)
        print(f"📖 {subject['name']} - Topics")
        print("=" * 40)

        print("1. Add Topic")
        print("2. View Topics")
        print("3. Start Study Session")
        print("4. Delete Topic")
        print("5. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("Topic name: ")

            topic = Topic(
                topic_id=str(uuid.uuid4()),
                subject_id=subject["subject_id"],
                user_id=user["uid"],
                name=name,
                created_at=datetime.now(),
                last_studied=datetime.now()
            )

            create_topic(topic)

            print("\n✅ Topic created successfully!")

        elif choice == "2":

            topics = get_topics(
                user["uid"],
                subject["subject_id"]
            )

            if len(topics) == 0:
                print("\nNo topics yet.")
                continue

            print()

            for index, topic in enumerate(topics, start=1):
                print(f"{index}. {topic['name']}")

        
        elif choice == "3":

            topics = get_topics(
             user["uid"],
             subject["subject_id"]
            )

            if len(topics) == 0:
              print("\n❌ No topics available.")
              continue

            print("\nSelect a topic:\n")

            for index, topic in enumerate(topics, start=1):
             print(f"{index}. {topic['name']}")

            try:
              choice = int(input("\nChoose topic: ")) - 1

              topic = topics[choice]

              manager = StudySessionManager()
              manager.start_session(
                 user,
                 subject,
                 topic
             )

            except (ValueError, IndexError):
                 print("\n❌ Invalid selection.")

        elif choice == "4":

            topics = get_topics(
                user["uid"],
                subject["subject_id"]
            )

            if len(topics) == 0:
                print("\nNo topics available.")
                continue

            for i, topic in enumerate(topics, start=1):
                print(f"{i}. {topic['name']}")

            index = int(input("\nChoose topic: ")) - 1

            delete_topic(
                user["uid"],
                subject["subject_id"],
                topics[index]["topic_id"]
            )

            print("\n🗑 Topic deleted!")

        elif choice == "5":
            break

        else:
            print("\n❌ Invalid choice.")