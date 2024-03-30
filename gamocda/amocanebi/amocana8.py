def lst_count(list):
    arr = []
    for num in list:
        arr.append(list.count(num)) 
        arr.sort() 
        if list.count(num) == arr[0]:
            print(num)
            break
        

ar = [ 0 , 0 , 5]
lst_count(ar)
