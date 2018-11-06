# 二分查找，时间复杂度O(logn)
def half_search(li, val):
    low = 0
    high = len(li)-1
    while low <= high:
        mid = (low+high)//2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            high = mid-1
        else:
            low = mid+1
    else:
        return None


v = half_search([1, 3, 5, 6, 7, 9, 10, 17], 7)
print(v)
