from utils import PhoneNumber


class TeleFormatter:
    formats = [
        {"prefix_size": 2, "example_phone_number": "XX-XXXX-XXXX"},
        {"prefix_size": 3, "example_phone_number": "XXX-XXX-XXXX"},
        {"prefix_size": 4, "example_phone_number": "XXXX-XX-XXXX"},
        {"prefix_size": 5, "example_phone_number": "XXXXX-X-XXXX"}
    ]

    def __init__(self, phone_number: str):
        self.phone_number = PhoneNumber(phone_number).clean()
        self.prefix = PhoneNumber(self.phone_number).get_prefix_match()
        self.formatted_phone_number = None

    def _set_example_phone_number(self):
        for _format in self.formats:
            if _format.get("prefix_size") == len(self.prefix):
                self.example_phone_number = _format.get("example_phone_number")
                return
        raise Exception(f"prefix: {self.prefix} corresponding format_size not found in {self.__class__.__name__}")

    def _find_hyphen_indexes(self):
        return [i for i, _ in enumerate(self.example_phone_number) if _ == "-"]

    def _add_hyphens(self):
        hyphen_indexes = self._find_hyphen_indexes()

        self.formatted_phone_number = list(self.phone_number)
        for i in hyphen_indexes:
            self.formatted_phone_number.insert(i, "-")
        self.formatted_phone_number = "".join(self.formatted_phone_number)

    def format(self):
        self._set_example_phone_number()
        self._add_hyphens()
        return self.formatted_phone_number