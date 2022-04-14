import os


def open_file(file_name: str):
    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, file_name)
    f = open(file_path, 'r')
    return f


class PhoneNumber:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def _strip_spaces(self):
        self.phone_number = self.phone_number.strip()

    def _remove_special_symbols(self):
        self.phone_number = self.phone_number.replace("-", "").replace(".", "").replace("．", "")

    def _ensure_number_is_string(self):
        _phone_number = ""
        for i in self.phone_number:
            try:
                _phone_number += str(int(i))
            except ValueError:
                continue
        self.phone_number = _phone_number

    def _get_area_codes(self):
        f = open_file("data/area_codes.txt")
        area_codes = f.read().split("\n")
        return area_codes

    def clean(self):
        self._strip_spaces()
        self._remove_special_symbols()
        self._ensure_number_is_string()
        return self.phone_number

    def get_prefix_match(self):
        _area_codes = self._get_area_codes()

        matches = []
        for area_code in _area_codes:
            if self.phone_number.startswith(area_code):
                matches.append(area_code)

        if matches:
            return max(matches, key=len)
        raise Exception("area code match not found")