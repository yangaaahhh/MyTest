# 斐波那契数列
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a + b
        n = n + 1


for i in fib(5):
    print(i)

