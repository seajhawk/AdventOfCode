from rich import print, inspect

with open('Day01/data.txt') as f:
    lines = f.readlines()

# inspect(lines)

previous = None
largerCount = 0

for line in lines:
    if len(line) > 0:
        line = int(line)
        if previous and line > previous:
            largerCount +=1
        previous = line

print(f"largerCount = {largerCount}")
print(f"Length = {len(lines)}")