from functools import reduce
even_numbers_list = [i for i in range(100, 1001)if i % 2 == 0]
print(reduce(lambda x, y: x * y, even_numbers_list))
