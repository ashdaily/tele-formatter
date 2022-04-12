```
> python3 main.py -n 0312345678 -c ja
03-1234-5678
> python3 main.py -n 0312345678 -c japan
03-1234-5678
> python3 main.py -n 0312345678 -c ja
03-1234-5678
> python3 main.py -n 0312345678 -c us
Traceback (most recent call last):
  File "/Users/ash/PycharmProjects/tel_formatter/main.py", line 28, in <module>
    result = main(phone_number, country_name)
  File "/Users/ash/PycharmProjects/tel_formatter/main.py", line 12, in main
    return TeleFormatter(phone_number, country_name).format()
  File "/Users/ash/PycharmProjects/tel_formatter/tele_formatter.py", line 33, in format
    factory_class = self._get_factory_class()
  File "/Users/ash/PycharmProjects/tel_formatter/tele_formatter.py", line 27, in _get_factory_class
    country = all_formatters.get(self.country_name)
  File "/Users/ash/PycharmProjects/tel_formatter/countries/countries_factory.py", line 15, in get
    raise NotImplementedError("Country not implemented, add a country in countries.countries_factory file")
NotImplementedError: Country not implemented, add a country in countries.countries_factory file
```

