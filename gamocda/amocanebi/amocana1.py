def even(lst):
    lstr = []
    for num in lst:
        if num % 2 == 0:
            lstr.append(str(num))
    sentence = "-".join(lstr)
    print(sentence)

list = [1,48,16,3]

even(list)