from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from datetime import date

# START ----- DatePicker class
class DatePicker(BoxLayout):
    """
    DatePicker is a UI component for selecting a date.
    
    It provides a default date as today's date and allows the user to pick a different date.
    """
    
    # START ----- init constructor
    def __init__(self, **kwargs):
        """
        Initialize the DatePicker with the given parameters.
        
        Args:
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        # Label to display the selected date
        self.date_label = Label(text=str(date.today()))
        self.add_widget(self.date_label)

        # Button to open the date picker popup
        self.select_date_button = Button(text="Select Date")
        self.select_date_button.bind(on_press=self.open_date_picker)
        self.add_widget(self.select_date_button)
    # END ----- init constructor

    # START ----- open_date_picker method
    def open_date_picker(self, instance):
        """
        Open the date picker popup to allow the user to select a date.
        
        Args:
            instance: The instance of the button that triggered this method.
        """
        content = GridLayout(cols=2)

        self.day_input = TextInput(text=str(date.today().day), multiline=False)
        self.month_input = TextInput(text=str(date.today().month), multiline=False)
        self.year_input = TextInput(text=str(date.today().year), multiline=False)

        content.add_widget(Label(text="Day:"))
        content.add_widget(self.day_input)
        content.add_widget(Label(text="Month:"))
        content.add_widget(self.month_input)
        content.add_widget(Label(text="Year:"))
        content.add_widget(self.year_input)

        submit_button = Button(text="Set Date")
        submit_button.bind(on_press=self.set_date)

        content.add_widget(submit_button)

        self.popup = Popup(title="Pick a Date", content=content, size_hint=(0.8, 0.8))
        self.popup.open()
    # END ----- open_date_picker method

    # START ----- set_date method
    def set_date(self, instance):
        """
        Set the date from the popup input fields.
        
        Args:
            instance: The instance of the button that triggered this method.
        """
        selected_date = date(int(self.year_input.text), int(self.month_input.text), int(self.day_input.text))
        self.date_label.text = str(selected_date)
        self.popup.dismiss()
    # END ----- set_date method
# END ----- DatePicker class
