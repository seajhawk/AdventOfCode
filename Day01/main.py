from rich import print, inspect

print("Hello World!")

with open('data.txt') as f:
    lines = f.readlines()

inspect(lines)
