import argparse

parser = argparse.ArgumentParser(description='Task about gold bars')

parser.add_argument('-W', type=int, help='--Capacity')
parser.add_argument('-w', type=int, help='--weights')
parser.add_argument('-n', type=int, help='--Number of bars')
args = parser.parse_args()

capacity = args.W
weights = args.w
bars_number = args.n

print(f"capacity = {capacity}")
print(f"weights = {weights}")
print(f"bars_number = {bars_number}")

golds = [0] + weights
gold_dict = {}
for i in range(0, capacity+1):
    gold_dict[(i, 0)] = 0
for i in range(0, bars_number+1):
    gold_dict[(0, i)] = 0
for i in range(1, bars_number+1):
    for weight in range(1, capacity+1):
        gold_dict[(weight, i)] = gold_dict[(weight, (i-1))]
        if golds[i] <= weight:
            val = gold_dict[(weight-golds[i], i-1)] + golds[i]
            if gold_dict[(weight, i)] < val:
                gold_dict[(weight, i)] = val

print(max(gold_dict.values()))
