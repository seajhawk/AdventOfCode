from rich import print, inspect

with open('data.txt') as f:
    lines = f.readlines()

# inspect(lines)

previous = 0
largerCount = 0

for line in lines:
    line = int(line)
    if line > previous:
        largerCount +=1
    previous = line

print(f"largerCount = {largerCount}")
print(f"Length = {len(lines)}")