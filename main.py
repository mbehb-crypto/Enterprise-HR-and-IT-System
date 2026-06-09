import sys
from employee import Employee
from audit import AuditLogger, save_to_db


def main():
    print("--- ContriPikin: Employee Management System ---")

    # Example raw payload parsin
    raw_payload = {"name": "Beltus MTbeh", "title": "Security Analyst"}

    try:
        # Pipeline mapping dictionary payload to object
        emp1 = Employee.from_dict(raw_payload)

        # Display initial profile
        print(f"\n--- Profile Created (Uncommitted) ---")
        print(f"Name:  {emp1.name}")
        print(f"Title: {emp1.title}")
        print("-" * 30)

        # Security Auditing Context Manager
        with AuditLogger(modifier_name="Admin_System_User") as audit_log:
            print("Changing employee name to Beltus Mbeh...")
            emp1.name = "Beltus Mbeh"

            # Save permanently
            save_to_db(emp1)
            print("Profile committed permanently to database.")

        # Display Final Profile
        print(f"\n--- Updated Profile (Committed) ---")
        print(f"Name:  {emp1.name}")
        print(f"Title: {emp1.title}")
        print("-" * 30)

    except ValueError as e:
        print(f"Validation Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"System Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()