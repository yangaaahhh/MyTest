# 快排
def quick_sort(array, left, right):
    # 第一个数大于最后一个数时，直接返回list
    if left < right:
        i, j = left, right
        # 设置基准数
        base = array[i]

        while i < j:
            # 从列表第 j 个元素往前判断，是否有大于或等于基准数的数
            # 有的话，就接着往前找
            while (i < j) and (array[j] >= base):
                j = j - 1
            # 如果找到比基准数小的，就将该值赋值给第 i 个元素
            array[i] = array[j]

            # 同样，从第 i 个元素往后找，是否有比基准数小或者等于的元素
            # 有的话，就接着往后找
            while (i < j) and (array[i] <= base):
                i = i + 1
            # 如果找到比基准数大的元素，就将该元素的值赋值给第 j 个元素
            array[j] = array[i]
        # 做完比较之后，列表被分为两部分，并且 i = j ，将该元素设置为base的值
        array[i] = base

        # 接下来，递归前半区和后半区
        quick_sort(array, left, i - 1)
        quick_sort(array, j + 1, right)
    return array


myarray = [10, 4, 2, 7, 9, 8, 6]
new_array = quick_sort(myarray, 0, len(myarray) - 1)

print(new_array)
