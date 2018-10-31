# 判断一个数是否是素数又是回文
def test(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    if str(n) == str(n)[::-1]:
        return True


l = []
for x in range(1000):
    if test(x):
        l.append(x)
print(l)
