from app.topic.topic_menu import topic_menu
from app.session.current_user import get_current_user


def show_subject_dashboard(subject):

    while True:

        print("\n" + "=" * 40)
        print(f"📘 {subject['name']}")
        print("=" * 40)

        print(f"Progress        : {subject['progress']}%")
        print(f"Topics          : {subject['total_topics']}")
        print(f"Study Hours     : {subject['study_hours']}")
        print(f"Priority        : {subject['priority']}")

        print("\nChoose an option")
        print("1. Continue Last Topic")
        print("2. Topics")
        print("3. Flashcards")
        print("4. Practice Questions")
        print("5. Mandatory Assessments")
        print("6. Analytics")
        print("7. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":
            print("\n🚧 Continue Last Topic coming soon!")

        elif choice == "2":
            topic_menu(subject, get_current_user())

        elif choice == "3":
            print("\n🚧 Flashcards coming soon!")

        elif choice == "4":
            print("\n🚧 Practice Questions coming soon!")

        elif choice == "5":
            print("\n🚧 Mandatory Assessments coming soon!")

        elif choice == "6":
            print("\n🚧 Analytics coming soon!")

        elif choice == "7":
            break

        else:
            print("\n❌ Invalid choice.")