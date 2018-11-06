# 选择排序，时间复杂度O(n2)
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i  # 假设当前最小的值的索引就是i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:  # min_loc 值如果发生过交换，表示最小的值的下标不是i,而是min_loc
            li[i], li[min_loc] = li[min_loc], li[i]
    return li


print(select_sort([2, 5, 1, 9, 3, 11, 7]))
