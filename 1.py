import argparse

parser = argparse.ArgumentParser(description='Simple math equations')

parser.add_argument('first_number', type=float, help='Input first number')
parser.add_argument('symbol', type=str, help='Input symbol')
parser.add_argument('second_number', type=float, help='Output second number')

args = parser.parse_args()

print(args)

action = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
}

result = action.get(args.symbol)
if result:
    result = result(args.first_number, args.second_number)
    print(result)
else:
    print("Error")
