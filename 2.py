import argparse
import math
import operator

parser = argparse.ArgumentParser()

parser.add_argument('symbol', type=str)
parser.add_argument('first_number', type=float)
parser.add_argument('second_number', type=float)

args = parser.parse_args()

try:
    function = getattr(math, args.symbol, False)
    if not function:
        function = getattr(operator, args.symbol)

    print(function(args.first_number, args.second_number))
except ZeroDivisionError:
    print("You can't divide by 0")
