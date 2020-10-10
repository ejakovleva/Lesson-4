def fact(n):
    x = 1
    for el in range(n):
        z = (el + 1) * x
        x = el + 1
        yield z


for i in fact(int(input("Enter a number you want to get the factorial for: "))):
    print(i)

