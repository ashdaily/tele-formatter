import argparse

from tele_formatter import TeleFormatter


def main(phone_number: str, country_name : str) -> str:
    """
    :type phone_number: str
    :type country_name: str
    :return: formatted phone number in string format as per country
    """
    return TeleFormatter(phone_number, country_name).format()


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number_to_format", type=str)
    parser.add_argument("-c", "--country", type=str)
    args = parser.parse_args()
    number = args.number_to_format
    country = args.country
    return number, country


if __name__ == '__main__':
    phone_number, country_name = collect_args()

    result = main(phone_number, country_name)
    print(result)