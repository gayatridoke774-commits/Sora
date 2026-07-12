from app.session.current_user import get_current_user
from app.session.session_manager import clear_session
from app.subject.subject_menu import subject_menu

def show_dashboard():
    user = get_current_user()

    while True:
        print("\n" + "=" * 40)
        print("        Welcome back to Sora ✨")
        print("=" * 40)

        if user:
            print(f"\nHello, {user['name']} 👋")
            print(f"Email: {user['email']}")

        print("""
1. Continue Studying
2. Subjects
3. Progress
4. Logout
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n🚧 Continue Study feature coming soon!")

        elif choice == "2":
            subject_menu()

        elif choice == "3":
            print("\n🚧 Progress Analytics coming soon!")

        elif choice == "4":
            clear_session()
            print("\n✅ Logged out successfully.")
            break

        else:
            print("\n❌ Invalid choice.")