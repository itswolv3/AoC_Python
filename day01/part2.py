from data import data

all_tots = []

for blck in data:
    # print(blck)
    block_tot = sum(blck)
    # print(block_tot)
    all_tots.append(block_tot)

sorted_tots = all_tots
sorted_tots.sort()

first = (sorted_tots[-1])
second = (sorted_tots[-2])
third = (sorted_tots[-3])

sum_biggest = first + second + third
print(sum_biggest)
