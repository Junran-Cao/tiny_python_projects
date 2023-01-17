#!/usr/bin/env python3
# the first line tells the operating system to use /usr/bin/env to find python3 to interpret this program.

"""
objective: to print some text
"""

# def main():
#     parser = argparse.ArgumentParser(description="Say hello")
#     # parser.add_argument("name", help="Name to greet")
#     parser.add_argument("-n", "--name", metavar="name",
#                         default="World", help="Name to greet")
#     args = parser.parse_args()
#
#     # print("Hello, World!")
#
#     print("Hello, " + args.name + "!")
#
# if __name__ == "__main__":
#     main()

import argparse


def get_args():
    parser = argparse.ArgumentParser(description="say Hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
