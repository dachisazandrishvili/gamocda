def word(lst):
    sentence = ""
    for char in lst:
        if int(char) > 0 or int(char) < 0:
            sentence += "N"
        elif int(char) == 0:
            sentence += "Z"
        else:
            sentence += "L"

    print(sentence)


list = ["0",0,0]

word(list)