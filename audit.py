from datetime import datetime
import sqlite3
from employee import Employee  # Make sure this matches your file name


class AuditLogger:
    def __init__(self, modifier_name: str):
        self.modifier = modifier_name

    def __enter__(self):
        # This was causing your previous "name 'datetime' is not defined" error
        print(f"[Audit Log] Session started by '{self.modifier}' at {datetime.now().isoformat()}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[Audit Log] Session terminated with error: {exc_val}")
        else:
            print("[Audit Log] Session closed successfully. Changes recorded.")
        return False  # Do not suppress exceptions; let main.py catch them


def save_to_db(employee: Employee, db_path: str = "company.db"):
    """Saves or updates the employee record in an actual SQLite Database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table schema dynamically if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            name TEXT NOT NULL,
            title TEXT NOT NULL
        )
    ''')

    # Insert the mapped employee data directly
    cursor.execute(
        "INSERT INTO employees (name, title) VALUES (?, ?)",
        (employee.name, employee.title)
    )

    conn.commit()
    conn.close()
    print(f"[DB] Successfully committed {employee.name} to {db_path}.")