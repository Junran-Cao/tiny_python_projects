#!/usr/bin/env python3

"""
We’re going on a picnic, and we want to print a list of items to bring along.
"""

import argparse


def get_args():
    """Get command-line inputs"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("items",
                        metavar="str",
                        nargs="+",  # The nargs '+' will make nargs accept one or more values.
                        type=str,
                        help="Item(s) to bring")

    parser.add_argument("-s", "--sorted",
                        help="Sort the items",
                        default=False,
                        action="store_true")

    return parser.parse_args()


def main():
    args = get_args()
    items = args.items  # a list with at least one element.
    sort_list = args.sorted

    if sort_list:
        items.sort(reverse=False)

    if len(items) == 1:
        print(
            "You are bringing {}.".format(
                items[len(items) - len(items)]
            )
        )

    elif len(items) == 2:
        print(
            "You are bringing {} and {}.".format(
                items[len(items) - len(items)], items[len(items) - len(items) + 1]
            )
        )

    elif len(items) > 2:
        print(
            "You are bringing {}{}.".format(
                ", ".join(items[:-1]), ", and " + items[-1]
            )
        )


if __name__ == '__main__':
    main()
