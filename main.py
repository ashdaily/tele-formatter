import argparse

from tele_formatter import TeleFormatter


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--phone_number", type=str)
    args = parser.parse_args()
    number = args.phone_number
    return number


if __name__ == '__main__':
    phone_number = collect_args()
    result = TeleFormatter(phone_number).format()
    print(result)