import unittest
from food_diary_extended import FoodDiary
from datetime import datetime
import json


class TestFoodDiaryExtended(unittest.TestCase):
    def setUp(self):
        self.food = FoodDiary()

    def test_get_current_date(self):
        date = datetime.now()
        current_date = '{}.{}.{}'.format(date.day, date.month, date.year)
        self.assertEqual(self.food.get_current_date(), current_date)

    def test_read_json_file(self):
        with open('food.json', 'r') as f:
            dict = json.load(f)

        self.assertEqual(self.food.read_json_file(), dict)

if __name__ == '__main__':
    unittest.main()
