def find_highest(lst):
	if len(lst) == 1:
        return lst[0]
	r = find_highest(lst[1:])
	return r if r>= lst[0] else lst[0]