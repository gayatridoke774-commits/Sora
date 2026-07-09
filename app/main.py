from app.auth.auth_service import register_user
from app.auth.auth_service import login_user
from app.session.session_manager import load_session
from app.session.current_user import set_current_user
from app.dashboard.dashboard import show_dashboard

def main():
      session = load_session()

      if session:
        set_current_user(session)
        show_dashboard()
        return
      while True:
        print("\n" + "=" * 40)
        print("         Welcome to Sora v1.0")
        print("=" * 40)
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n=== Create New User ===")

            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            result = register_user(name, email, password)

            if result["success"]:
                print("\n✅", result["message"])
                print("User ID:", result["uid"])
            else:
                print("\n❌ Registration Failed")
                print(result["message"])

        elif choice == "2":
            print("\n=== Login ===")

            email = input("Enter your email: ")
            password = input("Enter your password: ")

            result = login_user(
                email,
                password
            )

            if result["success"]:
                print("\n✅", result["message"])
            else:
                print("\n❌ Login Failed")
                print(result["message"])

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()