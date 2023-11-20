lst_1 = [0, 1, 0, 12, 3]
lst_2 = [0]
lst_3 = [2, 0, 13, 0, 0, 0, 5]
lst_4 = [9, 0, 7, 31, 0, 45, 0, 0, 45, 0, 0, 96, 0]
new_lst_1 = [el for el in lst_1 if el != 0]
quantity = len(lst_1) - len(new_lst_1)
new_lst_1 += [0 for _ in range(quantity)]
print(lst_1, "->", new_lst_1)
new_lst_2 = [el for el in lst_2 if el != 0]
quantity = len(lst_2) - len(new_lst_2)
new_lst_2 += [0 for _ in range(quantity)]
print(lst_2, "->", new_lst_2)
new_lst_3 = [el for el in lst_3 if el != 0]
quantity = len(lst_3) - len(new_lst_3)
new_lst_3 += [0 for _ in range(quantity)]
print(lst_3, "->", new_lst_3)
new_lst_4 = [el for el in lst_4 if el != 0]
quantity = len(lst_4) - len(new_lst_4)
new_lst_4 += [0 for _ in range(quantity)]
print(lst_4, "->", new_lst_4)
