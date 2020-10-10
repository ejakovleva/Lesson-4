from sys import argv

try:
    name, hours, rate, incentive = argv
    print(int(hours) * int(rate) + int(incentive))
except (NameError, ValueError):
    print("Enter 3 numbers!")

