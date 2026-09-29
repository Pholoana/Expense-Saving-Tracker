import sqlite3

DATABASE_NAME = "expense_tracker.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Create habits table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            periodicity TEXT NOT NULL
        )
    """)

    # Create savings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_id INTEGER NOT NULL,
            amount_saved REAL NOT NULL,
            saving_date DATE NOT NULL,
            FOREIGN KEY (habit_id) REFERENCES habits(id)
        )
    """)

    connection.commit()
    connection.close() 
    
def add_habit(name, amount, periodicity):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO habits (name, amount, periodicity)
        VALUES (?, ?, ?)
    """, (name, amount, periodicity))

    connection.commit()
    connection.close()


def get_all_habits():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, amount, periodicity
        FROM habits
        ORDER BY id
    """)

    habits = cursor.fetchall()

    connection.close()

    return habits

def delete_habit(habit_id):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM habits WHERE id = ?",
        (habit_id,)
    )

    connection.commit()
    connection.close()

def delete_all_habits():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM habits")

    connection.commit()
    connection.close()
    
def update_habit(habit_id, name, amount, periodicity):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE habits
        SET name = ?, amount = ?, periodicity = ?
        WHERE id = ?
    """, (name, amount, periodicity, habit_id))

    connection.commit()
    connection.close()
    
def add_saving(habit_id, amount_saved, saving_date):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO savings (habit_id, amount_saved, saving_date)
        VALUES (?, ?, ?)
    """, (habit_id, amount_saved, saving_date))

    connection.commit()
    connection.close()