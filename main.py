import argparse

from tele_formatter import TeleFormatter


def main(phone_number: str, country_name : str) -> str:
    """
    :type phone_number: str
    :type country_name: str
    :return: formatted phone number in string format as per country
    """
    return TeleFormatter(phone_number, country_name).format()


if __name__ == '__main__':
    """
        >> python3 main.py -n 0312345678 -c jp
        "03-1234-5678"
        >> python3 main.py -n ０３．１２３５．５６７８ -c jp
        "03-1234-5678"
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number_to_format", type=str)
    parser.add_argument("-c", "--country", type=str)
    args = parser.parse_args()
    number = args.number_to_format
    country = args.country

    main(number, country)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
