from employee import Employee

def main():
    # 1. Create an Employee object
    emp1 = Employee("Beltus MTbeh", "Cybersecurity")

    # 2. Display initial values (uses the getter implicitly)
    print(f"--- Initial Employee Details ---")
    print(f"Name: {emp1.name}")
    print(f"Title: {emp1.title}")
    print("-" * 30)

    # 3. Use the property setter to change the name
    print("Changing employee name to 'Beltus Mbeh'...")
    emp1.name = "Beltus Mbeh"

    # 4. Display the updated name
    print(f"\n--- Updated Employee Details ---")
    print(f"Name: {emp1.name}")
    print(f"Title: {emp1.title}")
    print("-" * 30)


if __name__ == "__main__":
    main()
