#!/usr/bin/env python3


import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dice_multiplier",
                        help="""this is the multiplier""")
    parser.add_argument("dice_sides",
                        help="""this is the number of sides""")
    parser.add_argument("additional_bonus",
                        help="""this is the aditional bonus""")

    args = parser.parse_args()
    mult = int(args.dice_multiplier)
    sides = int(args.dice_sides)
    bonus = int(args.additional_bonus)

    random.seed()
    randy = random.randrange(sides) + 1
    total = (mult * randy) + bonus

    message = str(mult) + "d" + str(sides) + "+" + str(bonus) + " ="
    print(message, total)


if __name__ == '__main__':
    main()
