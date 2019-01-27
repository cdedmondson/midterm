def aList(L1, L2):
    if len(L1) != len(L2):
        print("Error! lists are not the same size")

    count = len(L1) * 2
    list_of_tuples = []
    another_list_of_tuples = []
    is_first_max = 0
    negative_one_count = 0
    positive_one_count = 0

    for i in range(len(L2)):
        another_list_of_tuples.append(tuple((L1[i], L2[i])))

    while count != 0:
        pos = L1.index(max(L1))
        if L2[pos] != 1:
            negative_one_count += 1
            if negative_one_count == len(L2):
                print("(1) No max value with corresponding positive one exists")
            count -= 1
            L1.pop(pos)
            L2.pop(pos)
        else:
            is_first_max += 1
            positive_one_count += 1
            if is_first_max == 1:
                print("(1) Maximum value with corresponding 1: ", str(L1[pos]) + ',', L2[pos])
            list_of_tuples.append(tuple((L1[pos], L2[pos])))
            L1.pop(pos)
            L2.pop(pos)
            count -= 1
        count -= 1

    list_of_tuples.reverse()
    another_list_of_tuples.sort()
    print("(2)", another_list_of_tuples)
    if len(list_of_tuples) == 0:
        print("(3) No positive ones exist")
    else:
        print("(3)", list_of_tuples)


# Test 1
print("Test#1")
L1 = [13, 3, 25, 7, 21, 2, 50, 2, 13, 40, 34, 14, 6, 16]
L2 = [1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1]
aList(L1, L2)

# Test 2
print("Test#2")
L1 = [45, 21, 4, 31, 2]
L2 = [1, 1, 1, 1, 1]
aList(L1, L2)

# Test 3
print("Test#3")
L1 = [13, 3, 45]
L2 = [-1, -1, -1]
aList(L1, L2)
