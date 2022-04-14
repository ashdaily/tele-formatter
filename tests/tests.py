from unittest import TestCase

from tele_formatter import TeleFormatter


class TestTeleFormatter(TestCase):
    def test_phone_numbers_formatting_for_two_digit_prefix(self):
        phone_number = "0300000000"
        formatted_number = TeleFormatter(phone_number).format()
        self.assertEqual(formatted_number, "03-0000-0000")

    def test_phone_numbers_formatting_for_three_digit_prefix(self):
        phone_number = "0110000000"
        formatted_number = TeleFormatter(phone_number).format()
        self.assertEqual(formatted_number, "011-000-0000")

    def test_phone_numbers_formatting_for_four_digit_prefix(self):
        phone_number = "0123000000"
        formatted_number = TeleFormatter(phone_number).format()
        self.assertEqual(formatted_number, "0123-00-0000")

    def test_phone_numbers_formatting_for_four_digit_prefix(self):
        phone_number = "0126700000"
        formatted_number = TeleFormatter(phone_number).format()
        self.assertEqual(formatted_number, "01267-0-0000")

    def test_phone_numbers_formatting_with_zenkaku_characters(self):
        phone_number = "０３−００００−００００"
        formatted_number = TeleFormatter(phone_number).format()
        self.assertEqual(formatted_number, "03-0000-0000")

