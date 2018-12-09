def checker(word1, word2):
    list1 = []
    list2 = []
    list3 = []
    for i in word1:
        list1.append(ord(i))
    for j in word2:
        list2.append(ord(j))
    i = 0
    j = 0
    for k in range(len(list1)):
        list3.append(list1[i]-list2[j])
        i += 1
        j += 1
    count = 0
    for i in range(len(list3)):
        if list3[i] > 0 or list3[i] < 0:
            count += 1

    return count
