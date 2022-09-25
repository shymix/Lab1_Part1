import argparse

parser = argparse.ArgumentParser()
parser.add_argument('line', type=str)
args = parser.parse_args()

correct = True

symbols = "+-0123456789"
bad_operands = ["++", '+-', '-+', '--']
wrong_symbol = not all(symbol in symbols for symbol in args.line)
wrong_operand = any(operand in args.line for operand in bad_operands)

if wrong_symbol or wrong_operand:
    correct = False

if correct:
    try:
        print(correct, eval(args.line))
    except SyntaxError:
        print('False', 'None')
else:
    print(correct, 'None')
