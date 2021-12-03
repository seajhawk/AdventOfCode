from rich import print, inspect

with open('Day02/data.txt') as f:
    lines = list(map(int, f.readlines()))

# inspect(lines)

i = 0
previous = None
largerCount = 0
window = []
a = []
b = []
c = []

for i in range(len(lines)-3):
    a = lines[i:i+3]
    b = lines[i+1:i+4]

    asum = sum(a)
    bsum = sum(b)

    if bsum > asum:
        largerCount +=1
"""
    print(a)
    print(asum)
    print(b)
    print(bsum)
    print(bsum > asum)
    print()
"""

print(f"largerCount = {largerCount}")
print(f"TotalLength = {len(lines)}")
