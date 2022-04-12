from .base import Base


class Countries:
    list_of_countries = {}

    def add(self, cls):
        self.list_of_countries[cls.__name__.lower()] = cls
        for country_code in cls.country_code_strings:
            self.list_of_countries[country_code] = cls

    def get(self, country_name):
        if country_name is None:
            raise NotImplementedError("Country not implemented, add a country in countries.countries_factory file")
        return self.list_of_countries.get(country_name)


all_formatters = Countries()


@all_formatters.add
class Japan(Base):
    country_code_strings = {"ja", "jp"}
    country_code_number = "+81"
    example_phone_number = "3-1234-5678"
    prefix = "0"





