def rotate_list_slicing():
    test_list = [1, 4, 6, 7, 2]

    # printing original list
    print("Original list : " + str(test_list))

    # using slicing to left rotate by 3
    test_list = test_list[3:] + test_list[:3]

    # Printing list after left rotate
    print("List after left rotate by 3 : " + str(test_list))

    # using slicing to right rotate by 3
    # back to Original
    test_list = test_list[-3:] + test_list[:-3]

    # Printing after right rotate
    print("List after right rotate by 3(back to original) : "
          + str(test_list))


def rotate_list_collection_deque():
    from collections import deque

    # initializing list
    test_list = [1, 4, 6, 7, 2]

    # printing original list
    print("Original list : " + str(test_list))

    # using rotate() to left rotate by 3
    test_list = deque(test_list)
    test_list.rotate(-3)
    test_list = list(test_list)

    # Printing list after left rotate
    print("List after left rotate by 3 : " + str(test_list))

    # using rotate() to right rotate by 3
    # back to Original
    test_list = deque(test_list)
    test_list.rotate(3)
    test_list = list(test_list)

    # Printing after right rotate
    print("List after right rotate by 3(back to original) : "
          + str(test_list))


def rotate_list_pop_append():
    def leftRotate(l, d):
        for i in range(0, d):
            l.append(l.pop(0))

    l = [10, 20, 30, 40, 50]
    d = 3
    leftRotate(l, d)
    print(l)


def rotate_list_loop_swap():
    def reverse(l, b, e):
        while b < e:
            l[b], l[e] = l[e], l[b]
            b = b + 1
            e = e - 1

    def leftRotate(l, d):
        n = len(l)
        reverse(l, 0, d - 1)
        reverse(l, d, n - 1)
        reverse(l, 0, n - 1)

    l = [10, 20, 30, 40, 50]
    d = 3
    leftRotate(l, d)
    print(l)
