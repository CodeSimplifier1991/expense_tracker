"""
Main module for the Expense Tracker application.

This module initializes and runs the Kivy application.
"""

# Import the App class from the kivy.app module
from kivy.app import App

# Import the Dashboard class from our custom module
from kivy_app.ui.dashboard import Dashboard

# START ----- ExpenseTrackerApp class 
# Define a new class ExpenseTrackerApp that inherits from the App class
class ExpenseTrackerApp(App):
    """
    Main application class for the Expense Tracker.

    This class initializes the Dashboard and starts the Kivy application.
    """
    # The build method is called when the application starts
    def build(self):
        """
        Build the root widget of the application.

        Returns:
            Dashboard: The main dashboard widget of the application.
        """
        # Return an instance of the Dashboard class as the root widget
        return Dashboard()
# END ----- ExpenseTrackerApp class 

# This checks if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Create an instance of ExpenseTrackerApp and start the application
    ExpenseTrackerApp().run()
