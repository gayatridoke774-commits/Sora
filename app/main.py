from app.auth.auth_service import register_user


def main():
    while True:
        print("\n" + "=" * 40)
        print("         Welcome to Sora v1.0")
        print("=" * 40)
        print("1. Create User")
        print("2. Exit")

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
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()