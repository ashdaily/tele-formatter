from unittest import TestCase

from tele_formatter import TeleFormatter


class TestTeleFormatter(TestCase):
    test_fixtures = {
        "japan": {
            "country_names": ["jp", "ja", "japan", "JAPan", "Japan", "JAPAN"],
            "phone_numbers": ["0312345678", "０３．１２３４．５６７８"]
        }
    }

    def test_phone_numbers_formatting_for_japan(self):
        for _, test_data in self.test_fixtures.items():
            country_name_list = test_data.get("country_names")
            phone_number_list = test_data.get("phone_numbers")

            for country_name in country_name_list:
                for phone_number in phone_number_list:
                    formatted_number = TeleFormatter(phone_number, country_name).format()
                    self.assertEqual("03-1234-5678", formatted_number)