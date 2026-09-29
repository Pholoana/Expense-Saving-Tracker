from datetime import date

from database import (
    create_database,
    add_habit,
    update_habit,
    delete_habit,
    delete_all_habits,
    add_saving
)

from analytics import (
    get_all_habits,
    get_daily_habits,
    get_weekly_habits,
    get_longest_streak_overall,
    get_streak_per_habit,
    get_saving_progress
)

def main_menu():
    while True:
        print("\n" + "="*30)
        print("          MAIN MENU")
        print("="*30)
        print("1. Create habit")
        print("2. Edit habit")
        print("3. Delete habit")
        print("4. Record a saving")
        print("5. View habits")
        print("6. Exit")
        print("="*30)

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            create_habit()

        elif choice == "2":
            edit_habit()

        elif choice == "3":
            delete_habit_menu()

        elif choice == "4":
            record_saving()

        elif choice == "5":
            view_habits()

        elif choice == "6":
            print("\nGoodbye! Thanks for using the tracker.")
            break

def create_habit():
    print("\n" + "="*30)
    print("       CREATE HABIT")
    print("="*30)

    # Ask for habit name
    while True:
        habit_name = input("Enter habit name: ").strip()

        if habit_name:
            break
        else:
            print("Habit name cannot be empty.")

    # Ask for saving amount
    while True:
        amount = input("Enter saving amount: ").strip()

        try:
            amount = float(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Periodicity menu
    while True:
        print("\nSelect periodicity:")
        print("1. Daily")
        print("2. Weekly")

        choice = input("Select an option (1-2): ").strip()

        if choice == "1":
            periodicity = "Daily"
            break

        elif choice == "2":
            periodicity = "Weekly"
            break

        else:
            print("Invalid choice! Please select 1 or 2.")

    # Save habit
    add_habit(habit_name, amount, periodicity)

    print("\n" + "-"*30)
    print("       Habit Created!")
    print("-"*30)
    print(f"Name:        {habit_name}")
    print(f"Amount:      M{amount:.2f}")
    print(f"Periodicity: {periodicity}")
    print("*"*30)

def edit_habit():
    # Get all stored habits
    habits = get_all_habits()

    # Check if there are any habits
    if not habits:
        print("\nNo habits have been created yet.")
        return

    # Display all habits
    print("\n" + "="*40)
    print("            EDIT HABIT")
    print("="*40)

    print("Your habits:")
    print("-"*40)

    for habit in habits:
        print(
            f"{habit[0]}. {habit[1]} | "
            f"M{habit[2]:.2f} | {habit[3]}"
        )

    print("-"*40)

    # Ask user to select a habit
    while True:
        try:
            habit_id = int(
                input("Select the habit to edit: ")
            )

            # Find selected habit
            selected_habit = next(
                (habit for habit in habits if habit[0] == habit_id),
                None
            )

            if selected_habit:
                break
            else:
                print("Invalid habit number.")

        except ValueError:
            print("Please enter a valid number.")

    # Store current values
    name = selected_habit[1]
    amount = selected_habit[2]
    periodicity = selected_habit[3]

    # Edit menu
    while True:
        print("\n" + "="*30)
        print("          EDIT HABIT")
        print("="*30)

        print(f"Current name:        {name}")
        print(f"Current amount:      M{amount:.2f}")
        print(f"Current periodicity: {periodicity}")

        print("\nWhat would you like to edit?")
        print("1. Habit name")
        print("2. Saving amount")
        print("3. Periodicity")
        print("4. Save changes")
        print("5. Cancel")
        print("="*30)

        choice = input("Select an option (1-5): ").strip()

        # Edit name
        if choice == "1":

            while True:
                new_name = input(
                    "Enter new habit name: "
                ).strip()

                if new_name:
                    name = new_name
                    print("Habit name updated.")
                    break
                else:
                    print("Habit name cannot be empty.")

        # Edit amount
        elif choice == "2":

            while True:
                try:
                    new_amount = float(
                        input("Enter new saving amount: ")
                    )

                    if new_amount > 0:
                        amount = new_amount
                        print("Saving amount updated.")
                        break
                    else:
                        print("Amount must be greater than 0.")

                except ValueError:
                    print("Please enter a valid number.")

        # Edit periodicity
        elif choice == "3":

            while True:
                print("\nSelect new periodicity:")
                print("1. Daily")
                print("2. Weekly")

                periodicity_choice = input(
                    "Select an option (1-2): "
                ).strip()

                if periodicity_choice == "1":
                    periodicity = "Daily"
                    break

                elif periodicity_choice == "2":
                    periodicity = "Weekly"
                    break

                else:
                    print("Invalid choice. Please select 1 or 2.")

            print("Periodicity updated.")

        # Save changes
        elif choice == "4":

            update_habit(
                habit_id,
                name,
                amount,
                periodicity
            )

            print("\n" + "-"*30)
            print("  Habit Updated Successfully!")
            print("-"*30)
            print(f"Name:        {name}")
            print(f"Amount:      M{amount:.2f}")
            print(f"Periodicity: {periodicity}")
            print("*"*30)

            break

        # Cancel
        elif choice == "5":

            print("\nEdit cancelled.")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")

def delete_habit_menu():
    habits = get_all_habits()

    # Check if there are any habits
    if not habits:
        print("\nNo habits have been created yet.")
        return

    print("\n" + "="*30)
    print("          DELETE HABIT")
    print("="*30)
    print("1. Delete a habit")
    print("2. Delete all habits")
    print("3. Cancel")
    print("="*30)

    choice = input("Select an option (1-3): ").strip()

    # Delete one habit
    if choice == "1":

        print("\nYour habits:")
        print("-"*40)

        for habit in habits:
            print(
                f"{habit[0]}. {habit[1]} | "
                f"M{habit[2]:.2f} | {habit[3]}"
            )

        print("-"*40)

        try:
            habit_id = int(
                input("Select the habit to delete: ")
            )

            # Check if selected ID exists
            selected_habit = next(
                (habit for habit in habits if habit[0] == habit_id),
                None
            )

            if selected_habit:

                confirm = input(
                    f"Are you sure you want to delete "
                    f"'{selected_habit[1]}'? (y/n): "
                ).strip().lower()

                if confirm == "y":
                    delete_habit(habit_id)
                    print("\nHabit deleted successfully!")

                else:
                    print("\nDeletion cancelled.")

            else:
                print("\nInvalid habit number.")

        except ValueError:
            print("\nPlease enter a valid number.")

    # Delete all habits
    elif choice == "2":

        confirm = input(
            "Are you sure you want to delete ALL habits? (y/n): "
        ).strip().lower()

        if confirm == "y":
            delete_all_habits()
            print("\nAll habits have been deleted.")

        else:
            print("\nDeletion cancelled.")

    # Cancel
    elif choice == "3":
        print("\nDeletion cancelled.")

    else:
        print("\nInvalid choice. Please select 1, 2 or 3.")


def record_saving():
    
    # Get all stored habits
    habits = get_all_habits()

    # Check if there are any habits
    if not habits:
        print("\nNo habits have been created yet.")
        return

    print("\n" + "="*50)
    print("          RECORD A SAVING")
    print("="*50)

    # Display available habits
    print("Select a habit from the list below:")
    print("-"*50)

    for habit in habits:
        print(
            f"{habit[0]}. {habit[1]} | "
            f"Target: M{habit[2]:.2f} | "
            f"{habit[3]}"
        )

    print("-"*50)

    # Ask user to select a habit
    while True:
        try:
            habit_id = int(
                input("Select a habit (enter number): ")
            )

            selected_habit = next(
                (habit for habit in habits if habit[0] == habit_id),
                None
            )

            if selected_habit:
                break
            else:
                print("Invalid habit number.")

        except ValueError:
            print("Please enter a valid number.")

    # Ask for amount saved
    while True:
        try:
            amount_saved = float(
                input("Enter amount saved: ")
            )

            if amount_saved > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    # Get today's date
    saving_date = date.today().isoformat()

    # Save the record
    add_saving(
        habit_id,
        amount_saved,
        saving_date
    )

    print("\n")
    print("       Saving Recorded!")
    print("-"*40)
    print(f"Habit:        {selected_habit[1]}")
    print(f"Amount saved: M{amount_saved:.2f}")
    print(f"Date:         {saving_date}")
    print("-"*40)

def view_habits():
    while True:
        print("\n" + "="*30)
        print("        HABIT ANALYTICS")
        print("="*30)

        print("1. View all habits")
        print("2. Daily habits")
        print("3. Weekly habits")
        print("4. Longest streak overall")
        print("5. Streak per habit")
        print("6. Saving progress")
        print("7. Return to main menu")

        print("="*30)

        choice = input("Select an option (1-7): ").strip()

        # View all habits
        if choice == "1":

            habits = get_all_habits()

            print("\n")
            print("              ALL HABITS")
            print("-"*40)

            if not habits:
                print("No habits have been created yet.")
            else:
                for habit in habits:
                    print(
                        f"{habit[0]}. {habit[1]} | "
                        f"M{habit[2]:.2f} | "
                        f"{habit[3]}"
                    )

            print("-"*40 + "\n")

        # Daily habits
        elif choice == "2":

            habits = get_daily_habits()

            print("\n")
            print("             DAILY HABITS")
            print("-"*40)

            if not habits:
                print("No daily habits found.")
            else:
                for habit in habits:
                    print(
                        f"{habit[0]}. {habit[1]} | "
                        f"M{habit[2]:.2f} | "
                        f"{habit[3]}"
                    )
                    
            print("-"*40 + "\n")

        # Weekly habits
        elif choice == "3":

            habits = get_weekly_habits()

            print("\n")
            print("            WEEKLY HABITS")
            print("-"*40)

            if not habits:
                print("No weekly habits found.")
            else:
                for habit in habits:
                    print(
                        f"{habit[0]}. {habit[1]} | "
                        f"M{habit[2]:.2f} | "
                        f"{habit[3]}"
                    )
                    
            print("-"*40 + "\n")

        # Longest streak overall
        elif choice == "4":

            result = get_longest_streak_overall()

            print("\n")
            print("        LONGEST STREAK OVERALL")
            print("-"*40)

            if result and result[2] > 0:
                print(f"Habit: {result[1]}")
                print(f"Recorded savings: {result[2]}")
            else:
                print("No savings have been recorded yet.")
                
            print("-"*40 + "\n")

        # Streak per habit
        elif choice == "5":

            results = get_streak_per_habit()

            print("\n")
            print("          STREAK PER HABIT")
            print("-"*40)

            for result in results:
                print(
                    f"{result[1]}: "
                    f"{result[2]} recorded savings"
                )
                
            print("-"*40 + "\n")
        
        # Saving progress
        elif choice == "6":
        
            results = get_saving_progress()
        
            print("\n")
            print("                        SAVING PROGRESS")
            print("-"*70)
        
            if not results:
                print("No habits have been created yet.")
        
            else:
                print(
                    f"{'Habit':<25}"
                    f"{'Target':<15}"
                    f"{'Saved':<15}"
                    f"{'Status':<15}"
                )
        
                print("-"*70)
        
                for result in results:
        
                    habit_name = result[1]
                    target_amount = result[2]
                    saved_amount = result[3]
        
                    # Determine status
                    if saved_amount == 0:
                        status = "Not started"
        
                    elif saved_amount < target_amount:
                        status = "In progress"
        
                    else:
                        status = "Completed"
        
                    print(
                        f"{habit_name:<25}"
                        f"M{target_amount:<14.2f}"
                        f"M{saved_amount:<14.2f}"
                        f"{status:<15}"
                    )
        
            print("-"*70 + "\n")
        
        # Return to main menu
        elif choice == "7":
            break
        
        else:
            print("\nInvalid choice. Please select 1-7.")

if __name__ == "__main__":
    create_database()
    main_menu()