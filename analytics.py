import sqlite3

DATABASE_NAME = "expense_tracker.db"

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

def get_daily_habits():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, amount, periodicity
        FROM habits
        WHERE periodicity = 'Daily'
        ORDER BY id
    """)

    habits = cursor.fetchall()

    connection.close()

    return habits

def get_weekly_habits():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, amount, periodicity
        FROM habits
        WHERE periodicity = 'Weekly'
        ORDER BY id
    """)

    habits = cursor.fetchall()

    connection.close()

    return habits

def get_longest_streak_overall():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            habits.id,
            habits.name,
            COUNT(savings.id) AS saving_count
        FROM habits
        LEFT JOIN savings
            ON habits.id = savings.habit_id
        GROUP BY habits.id, habits.name
        ORDER BY saving_count DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def get_streak_per_habit():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            habits.id,
            habits.name,
            COUNT(savings.id) AS saving_count
        FROM habits
        LEFT JOIN savings
            ON habits.id = savings.habit_id
        GROUP BY habits.id, habits.name
        ORDER BY habits.id
    """)

    results = cursor.fetchall()

    connection.close()

    return results

def get_saving_progress():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            habits.id,
            habits.name,
            habits.amount,
            COALESCE(SUM(savings.amount_saved), 0) AS saved_amount
        FROM habits
        LEFT JOIN savings
            ON habits.id = savings.habit_id
        GROUP BY habits.id, habits.name, habits.amount
        ORDER BY habits.id
    """)

    results = cursor.fetchall()

    connection.close()

    return results