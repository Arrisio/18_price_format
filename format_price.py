import argparse


def format_price(price):
    if isinstance(price, str):
        price = price.replace(',', '.')
        price = price.replace(' ', '')

    try:
        return (
            '{:,.2f}'.format(float(price)).replace(',', ' ').replace('.00', '')
        )
    except (ValueError, TypeError):
        return


def parse_arguments():
    parser = argparse.ArgumentParser('set price to be formated with key -p')

    parser.add_argument(
        '-p', '-price', action='store',
        dest='price',
        help='price ',
        required=True
    )

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    print('Formated price is: {}'.format(format_price(args.price)))
