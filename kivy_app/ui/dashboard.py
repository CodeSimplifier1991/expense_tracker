# Import the App class from the kivy.app module
from kivy.app import App

# Import the BoxLayout class from the kivy.uix.boxlayout module
from kivy.uix.boxlayout import BoxLayout

# Import the Label class from the kivy.uix.label module
from kivy.uix.label import Label

# Import the TextInput class from the kivy.uix.textInput module
from kivy.uix.textinput import TextInput

# Import the Button class from the kivy.uix.button module
from kivy.uix.button import Button

# Import the ListView and ListItemButton classes from kivy.uix.listview module
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout


# Import the StringProperty from the kivy.properties module
from kivy.properties import StringProperty

# START ----- Dashboard class inherits from BoxLayout class
class Dashboard(BoxLayout):
    """
    Dashboard is a UI component for the Expense Tracker application.
    
    It provides a user interface for displaying the current balance, 
    and for adding income and expense entries.
    """
    # START ----- init constructor
    def __init__(self, **kwargs):
        """
        Initialize the Dashboard with the given parameters.
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        """
        # Call the initializer of the parent class (BoxLayout) with any keyword arguments
        super().__init__(**kwargs)

        # Displays the Dashboard vertically
        self.orientation = 'vertical'

        # Shows the balance text as a widget
        self.balance_label = Label(text="Current Balance: $0")
        self.add_widget(self.balance_label)

        # Enables the user to enter an amount using the text input
        self.amount_input = TextInput(hint_text="Enter amount", multiline=False)
        self.add_widget(self.amount_input)

        # Shows the "Add Income" as a widget
        self.add_income_button = Button(text="Add Income")
        self.add_income_button.bind(on_press=self.add_income) # Calls the add_income method on press button event
        self.add_widget(self.add_income_button)

        # Shows the "Add Expense" as a widget
        self.add_expense_button = Button(text="Add Expense")
        self.add_expense_button.bind(on_press=self.add_expense) # Calls the add_expense method on press button event
        self.add_widget(self.add_expense_button)

        # Create a RecycleView widget to display entries and add it to the Dashboard
        self.entries_list = RecycleView()
        self.entries_list.viewclass = 'Label'
        self.entries_layout = RecycleBoxLayout(orientation='vertical', default_size=(None, 40), size_hint_y=None)
        self.entries_layout.bind(minimum_height=self.entries_layout.setter('height'))
        self.entries_list.add_widget(self.entries_layout)
        self.add_widget(self.entries_list)

        # Initialize balance and entries list
        self.balance = 0
        self.entries = []

    # END ----- init constructor
    
    # START ----- add_income method
    def add_income(self, instance):
        """
        Add an income entry to the dashboard.
        
        Args:
            instance: The instance of the button that triggered this method.
        """
        amount = float(self.amount_input.text)
        self.balance += amount # Adds the amount to the balance
        self.update_balance_label()
    # END ----- add_income method

    # START ----- add_expense method
    def add_expense(self, instance):
        """
        Add an expense entry to the dashboard.
        
        Args:
            instance: The instance of the button that triggered this method.
        """
        amount = float(self.amount_input.text)
        self.balance -= amount # Deducts the amount from the balance
        self.entries.append(f"Expense: -${amount}") # Add the entry to the entries list
        self.update_balance_label()
    # END ----- add_expense method
    
    # START ----- update_balance method
    def update_balance_label(self):
        """
        Update the balance label to reflect the current balance.
        """
        self.balance_label.text = f"Current Balance: ${self.balance: .2f}"
    # END ----- update_balance method

    # START ----- update_entries_list method
    def update_entries_list(self):
        """
        Update the entries list to display the current entries.
        """
        self.entries_list.data = [{'text': entry} for entry in self.entries]
    # END ----- update_entries_list method


# END ----- Dashboard class inherits from BoxLayout class