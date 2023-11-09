def find_highest(lst):
    if len(lst) == 1:
        return lst
    if lst[0] < lst[1]:
        lst.pop(0)
    else:
        lst.pop(1)
    return find_highest(lst)


lst = [1, 6, 8, 3, 4, 3]
print(find_highest(lst))
