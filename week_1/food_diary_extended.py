from datetime import datetime
import json


class FoodDiary:

    def __init__(self):
        self._file = 'food.json'

    def get_current_date(self):
        date = datetime.now()

        return '{}.{}.{}'.format(date.day, date.month, date.year)

    def read_json_file(self):
        with open(self._file, 'r') as f:
            dict = json.load(f)
        return dict

    def add_meal(self, meal):
        pass

    def list_meal(self, current_date):
        pass


class CLI:

    def __init__(self):
        pass

    def menu_message(self):
        pass

    def help_message(self):
        pass

    def start_program(self):
        pass

    def _write_json_file(self, diary):
        pass

    def _read_json_file(self):
        pass
