from requests import Request
from rich import print

data = Request(method="get", url="https://adventofcode.com/2021/day/1/input")

print(data)
