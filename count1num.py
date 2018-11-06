# 统计整型数的二进制包含多少个1
def count1num(num):
    count = 0
    while 0 != num:
        count += 1
        num = num & (num - 1)
    return count


print(count1num(5))
print(bin(5))
