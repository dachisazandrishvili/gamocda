def sortt(lst):
    new_l = []
    new_ll = []
    for char in lst:
        for st in char:
            m = char.count(st)
            new_ll.append(m)
            new_ll.sort()
            
        for n in new_ll:
            n = str(n)
            new_l.insert(char,new_ll.index(n))
    return new_l
