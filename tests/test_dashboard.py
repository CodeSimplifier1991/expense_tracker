import unittest
from kivy_app.ui.dashboard import Dashboard

# START ----- TestDashboardClass class
class TestDashboardClass(unittest.TestCase):

    # START ----- setUp() method
    def setUp(self):
        """Set up test environment before each test"""
        self.dashboard = Dashboard()
    # END ----- setUp() method

    
    # START ----- test_add_income_method method
    def test_add_income_method(self):
        """Test adding income updates the balance correctly."""
        initial_balance = self.dashboard.balance
        self.dashboard.amount_input.text = '100'
        self.dashboard.add_income(None)
        
        self.assertEqual(self.dashboard.balance, initial_balance + 100)
        self.assertEqual(self.dashboard.balance_label.text, f"Current Balance: ${initial_balance + 100}")
    # END ----- test_add_income_method method

    
    # START ----- test_add_expense_method method
    def test_add_expense_method(self):
        """Test adding expense updates the balance correctly."""
        initial_balance = self.dashboard.balance
        self.dashboard.amount_input.text = '50'
        self.dashboard.add_expense(None)
        
        self.assertEqual(self.dashboard.balance, initial_balance - 50)
        self.assertEqual(self.dashboard.balance_label.text, f"Current Balance: ${initial_balance - 50}")
    # END ----- test_add_expense_method method

# END ----- TestDashboardClass class

if __name__ == '__main__':
    unittest.main()
