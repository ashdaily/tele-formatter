from countries.countries_factory import all_formatters


class TeleFormatter:
    def __init__(self, phone_number: str, country_name: str):
        self.phone_number = phone_number
        self.country_name = country_name.lower()

    def _strip_spaces(self):
        # trim spaces
        self.phone_number = self.phone_number.strip()
        self.country_name = self.country_name.strip()

    def _remove_special_symbols(self):
        self.phone_number = self.phone_number.replace("-", "").replace(".","").replace("．", "")

    def _ensure_number_in_string(self):
        self.phone_number = int(self.phone_number)
        self.phone_number = str(self.phone_number)

    def _clean(self):
        self._strip_spaces()
        self._remove_special_symbols()
        self._ensure_number_in_string()

    def _get_factory_class(self):
        country = all_formatters.get(self.country_name)
        return country

    def format(self):
        self._clean()


        factory_class = self._get_factory_class()

        return factory_class(self.phone_number).format()






