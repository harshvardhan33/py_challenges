
list1 = []
while True:
    str1 = input()
    if not str1:
        break
    tup1 = str1.split(',')
    list1.append((tup1[0], int(tup1[1]), int(tup1[2])))
