import unittest
from unittest.mock import patch
from src.input_functions import get_athlete_name, get_training_plan, get_current_weight, get_weight_category


class TestInputFunctions(unittest.TestCase):

    @patch('builtins.input', return_value="John Doe")
    def test_get_athlete_name(self, mock_input):
        self.assertEqual(get_athlete_name(), "John Doe")

    @patch('builtins.input', return_value="Intermediate")
    def test_get_training_plan(self, mock_input):
        self.assertEqual(get_training_plan(), "Intermediate")

    @patch('builtins.input', return_value="75")
    def test_get_current_weight(self, mock_input):
        self.assertEqual(get_current_weight(), 75.0)

    @patch('builtins.input', return_value="Middleweight")
    def test_get_weight_category(self, mock_input):
        self.assertEqual(get_weight_category(), "Middleweight")


# Add more tests as needed, especially for edge cases or invalid inputs

if __name__ == "__main__":
    unittest.main()
