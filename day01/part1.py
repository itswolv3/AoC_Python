from data import data

all_tots = []

for blck in data:
    # print(blck)
    block_tot = sum(blck)
    print(block_tot)
    all_tots.append(block_tot)

print("Biggest tot")
print(max(all_tots))
