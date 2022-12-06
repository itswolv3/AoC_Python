

with open("origin_data.txt", "r") as f:
    data = f.readlines()

new_data = []

for i in range(0, 5):
    new_pair = data[i].split()
    new_data.append(new_pair)

print(new_data)
