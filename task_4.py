initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
final_list = [i for i in initial_list if initial_list.count(i) == 1]
print(final_list)
