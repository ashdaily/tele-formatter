class Base:
    country_code_number = None
    country_code_strings = set()
    country_code_number = None
    example_phone_number = None
    prefix = "0"

    def __init__(self, phone_number : str):
        """
        :type phone_number: should be a phone number of type string
        """
        self.phone_number = phone_number

    def _remove_country_code_prefix(self):
        if self.country_code_number.startswith(self.country_code_number):
            self.phone_number = self.phone_number.removeprefix(self.country_code_number)

    def _find_hyphen_indexes(self):
        return [i for i, _ in enumerate(self.example_phone_number) if _ == "-"]

    def _add_hyphens(self):
        hyphen_indexes = self._find_hyphen_indexes()

        self.phone_number = list(self.phone_number)
        for i in hyphen_indexes:
            self.phone_number.insert(i, "-")
        self.phone_number = "".join(self.phone_number)

    def _prefix(self):
        self.phone_number = self.prefix + self.phone_number

    def format(self):
        self._add_hyphens()
        self._prefix()
        return self.phone_number
