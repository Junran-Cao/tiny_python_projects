#!/usr/bin/env python3

"""
Instruction:
This program is to accept a single positional argument and will print the given argument inside the “Ahoy” bit,
along with the word “a” or “an” depending on whether the argument starts with a consonant or a vowel.
"""

import argparse


def get_args():
    """Here to obtain input arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",  # this provides the --help
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('positional',  # this is the Namespace
                        metavar='word',
                        help='A word')

    return parser.parse_args()


def main():
    args = get_args()
    word = args.positional

    initial_letter = word[0].upper()
    if initial_letter in "AEIOU":
        article = "an"
    else:
        article = "a"

    # print("Ahoy, Captain, " + article + " " + word + " off the larboard bow!")
    print("Ahoy, Captain, {} {} off the larboard bow!".format(article,word))

    # article_v2 = "a" if word[0].lower() not in "aeiou" else "an"
    # print("I repeat: " + article_v2 + " " + word + " !!")
    # print(f"I repeat: {article_v2} {word}!!")


if __name__ == '__main__':
    main()
