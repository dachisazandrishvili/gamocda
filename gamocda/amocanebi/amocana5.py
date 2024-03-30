def sortt(lst):
    new_l = []
    for char in lst:
        new_l.append(len(char))
        new_l.sort()
        if new_l[0] == len(char):

