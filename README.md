# Expense-Saving-Tracker

Project Overview

The Expense Saving Tracker is a Python-based command-line habit tracking application designed to help users build a habit of saving towards a specific financial target. The application allows users to create saving habits, define a target amount and choose a saving periodicity of Daily or Weekly. Users can then record their actual savings and analyse their progress towards their targets.

The project was developed as part of a Python programming assignment with a focus on object-oriented programming (OOP), functional programming, persistent data storage and user interaction through a command-line interface (CLI).


Features

The application provides the following main features:

1. Create a Habit

    Users can create a new saving habit by entering:
    * Habit name
    * Target saving amount
    * Periodicity
    
    Available periodicities are:
    * Daily
    * Weekly
    
    Example:
    
    Habit name: Save for Fuel
    Target amount: M20
    Periodicity: Daily


2. Edit a Habit

    Users can select an existing habit and modify:
    * Habit name
    * Target saving amount
    * Periodicity
    
    Changes are saved to the database.


3. Delete a Habit

    Users can:
    * Delete a specific habit
    * Delete all existing habits
    
    The application asks for confirmation before deleting habits.


4. Record a Saving

    Users can select one of their existing habits and enter the amount they have saved.
    
    The application automatically records the date of the saving.
    
    Example:
    
    Habit: Save for Fuel
    Amount saved: M20
    Date: 2026-09-29
    
    Each saving is associated with the relevant habit in the database.


5. View Habits and Analytics

    The application provides an analytics menu:
    
    1. View all habits
    2. Daily habits
    3. Weekly habits
    4. Longest streak overall
    5. Streak per habit
    6. Saving progress
    
    Saving Progress
    Saving progress compares the total amount saved for each habit against its target.
    
    Each habit is assigned one of three statuses:

    * Not started — no savings have been recorded.
    * In progress — savings have been recorded, but the target is not met yet.
    * Completed — the total savings are equal to or greater than the target.
    
    Technology Used
    
    The application was developed using:
    * Python 3
    * SQLite
    * Command-Line Interface (CLI)
    * Object-Oriented Programming concepts
    * Functional Programming concepts

    The application uses Python's built-in libraries and does not require external Python packages.


6. Project Structure
    
    The final project consists of three main Python modules:
    
    a) main.py
        main.py contains the main application flow and user interaction.
    
        It contains:
        * Main menu
        * Create habit functionality
        * Edit habit functionality
        * Delete habit functionality
        * Record saving functionality
        * Navigation between menus
        * User input validation
    
    b) database.py
        database.py manages the application's SQLite database.
        
        It is responsible for:
        * Creating the database
        * Creating the required tables
        * Adding habits
        * Retrieving habits
        * Updating habits
        * Deleting individual habits
        * Deleting all habits
        * Recording savings
    
        The database provides persistent storage, meaning that information remains available after the application is closed.
        
        The database contains two tables:
        
        i. habits
        Stores information about each saving habit.
          
            id, name, amount, periodicity.
        
        ii. savings
        Stores individual saving records.
    
            id, habit_id, amount_saved, saving_date.
    
        The habit_id connects each saving to its corresponding habit.


    c) analytics.py

        analytics.py is responsible for retrieving and analysing information from the database.
        
        It provides functionality for:
        * Viewing all habits
        * Filtering Daily habits
        * Filtering Weekly habits
        * Calculating the habit with the highest number of recorded savings
        * Calculating recorded savings per habit
        * Calculating saving progress
        
        The analytics functionality retrieves the relevant data from the database and presents the results to the user through the main application.


7. Database Relationship

    The application uses a relationship between the habits and savings tables.
    
    HABITS
    |
    habit_id
    |
    SAVINGS

    One habit can have multiple saving records.
    
    For example:
    
    Save for Vacation
           M50  → 2026-09-01
           M30  → 2026-09-08
           M40  → 2026-09-15
           M20  → 2026-09-22
    
    The total saved for the habit would be: M50 + M30 + M40 + M20 = M140


9. Installation

    The application requires:
    
    * Python 3.x
    * An environment capable of running Python programs, such as Anaconda/Spyder, VS Code or a standard Python terminal.
    
    No external Python packages are required.


10. Running the Application

    Clone or download the project from GitHub.
        git clone <YOUR-GITHUB-REPOSITORY-LINK>
    
    Navigate to the project directory:
        cd Expense-Saving-Tracker
    
    Run the application:
        python main.py
    
    If using Anaconda/Spyder, open main.py and run the file.
    
    The application will automatically create the SQLite database if it does not already exist.


11. Main Menu

    When the application starts, the user is presented with the following menu:
    
    ==============================
              MAIN MENU
    ==============================
    1. Create habit
    2. Edit habit
    3. Delete habit
    4. Record a saving
    5. View habits
    6. Exit
    ==============================
    
    The user selects an option by entering the corresponding number.


12. Data Persistence

    The application uses SQLite for persistent data storage.
    
    The database file is: expense_tracker.db
    
    The database is created automatically by database.py.
    
    This allows users to close and reopen the application without losing their existing habits and saving records.


13. Analytics
    
    The analytics functionality allows users to understand their saving activity.
    
    a) Longest Streak Overall
        In the current implementation, the "Longest Streak Overall" identifies the habit with the highest number of recorded savings.
        
        For example:
        
        Save for Fuel       → 5 recorded savings
        Save for Bicycle    → 8 recorded savings
        
        The application identifies:
        Save for Bicycle
        8 recorded savings
    
    b) Streak Per Habit
    The application also displays the number of recorded savings associated with each habit.
    
    c) Saving Progress
        The application calculates the total amount saved for each habit and compares it with the target.
        
        Example:
            
        Habit              Target       Saved        Status
        ---------------------------------------------------------
        Save for Fuel      M20.00       M20.00       Completed
        Save for Bicycle   M50.00       M30.00       In progress
        Vacation           M100.00      M0.00        Not started


14. Design Decisions

    The final implementation uses three Python modules rather than the five modular structure initially planned.
    
    The original concept was:
        main.py
        database.py
        analytics.py
        cli.py
        habit_manager.py
        habit.py
    
    The final implementation:
        main.py
        database.py
        analytics.py
    
    This approach allowed the application to remain functional while still maintaining separation between the main application flow, database operations and analytics.


15. Future Improvements

    Possible improvements for future versions include:
    
    i.Graphical User Interface
        A GUI could make the application more visually appealing and easier to use. It could also provide visual feedback or animations when a saving target is reached.
    
    ii. Reminder Notifications
    The application could send reminders based on the periodicity of each habit.
    For example:
        * Daily habit → daily reminder
        * Weekly habit → weekly reminder
    
    iii. Advanced Analytics
    Future versions could provide:
        * Saving trends
        * Monthly and yearly summaries
        * Progress charts
        * Saving patterns
        * Actionable financial suggestions
        * More advanced financial analytics
    
    iv. More Accurate Streak Calculation
        The current implementation counts recorded savings when analysing streak-related information. A future version could use the actual saving dates and periodicity to calculate true consecutive Daily or Weekly streaks.


16. Author

    Nkopane Pholoana**
    Expense Saving Tracker
    
    GitHub Repository:
    
    https://github.com/Pholoana/Expense-Saving-Tracker.git

License

This project was developed as part of an academic project and is intended primarily for educational purposes.
