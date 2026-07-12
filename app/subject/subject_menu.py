import uuid

from app.subject.subject_dashboard import show_subject_dashboard

from app.models.subject import Subject
from app.services.subject_servics import (
    create_subject,
    get_subjects,
    delete_subject
)
from app.session.current_user import get_current_user
from datetime import datetime


def subject_menu():

    user = get_current_user()

    while True:

        print("\n========== SUBJECTS ==========")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Delete Subject")
        print("4. Back")

        choice = input("\nEnter choice: ")

        if choice == "1":

            name = input("Subject Name: ")

            subject = Subject(
                subject_id=str(uuid.uuid4()),
                user_id=user["uid"],
                name=name,
                created_at=datetime.now(),
                last_studied=datetime.now()
            )

            create_subject(subject)

            print("\n✅ Subject created successfully!")

        elif choice == "2":

            subjects = get_subjects(user["uid"])

            if len(subjects) == 0:
                print("\nNo subjects found.")
                continue

            print("\nYour Subjects:\n")

            for index, subject in enumerate(subjects, start=1):
                print(f"{index}. {subject['name']}")

            choice = input("\nSelect subject (0 to go back): ")

            if choice == "0":
                continue

            try:
             subject = subjects[int(choice) - 1]
             show_subject_dashboard(subject)
            except (ValueError, IndexError):
                print("\n❌ Invalid selection.")

        elif choice == "3":

            subjects = get_subjects(user["uid"])

            if len(subjects) == 0:
                print("No subjects available.")
                continue

            for i, subject in enumerate(subjects, start=1):
                print(f"{i}. {subject['name']}")

            index = int(input("\nChoose subject: ")) - 1

            delete_subject(
                user["uid"],
                subjects[index]["subject_id"]
            )

            print("\n🗑 Subject deleted!")

        elif choice == "4":
            break