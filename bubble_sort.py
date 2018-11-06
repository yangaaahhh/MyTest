# 冒泡排序，flag标志位，判断是否一开始就已经排好,最差情况下，时间复杂度O(n2)
def bubble_sort(li):
    for j in range(len(li) - 1):
        flag = False
        for i in range(1, len(li)):
            if li[i] > li[i - 1]:
                li[i], li[i-1] = li[i-1], li[i]
                flag = True
        if not flag:
            return li
    return li


print(bubble_sort([2, 5, 1, 9, 3, 4, 10, 8]))
