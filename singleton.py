# 装饰器实现的单例模式
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class A(object):
    def __init__(self, x):
        self.x = x


a1 = A(2)
a2 = A(3)
print(id(a1))
print(id(a2))
print(a1.x)
print(a2.x)
