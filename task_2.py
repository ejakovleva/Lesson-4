# 1 вариант решения
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [j for i, j in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(my_new_list)


#  2 вариант решения (если данные надо было запрашивать)
# my_list = input("Enter numbers split by a tab: ").split()
# try:
#     my_new_list = [int(j) for i, j in enumerate(my_list) if int(my_list[i]) > int(my_list[i - 1]) and i != 0]
# except ValueError:
#     print('Enter numbers!')
# print(my_list)
# print(my_new_list)
