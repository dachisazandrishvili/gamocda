def shortest(lst):
    newlst =[]
    for char in lst:
        newlst.append(len(char))
        newlst.sort()
        if len(char) == newlst[0]:
            print(char)

list = ["hi", "hello"]

shortest(list)
