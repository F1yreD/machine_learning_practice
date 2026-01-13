# 作者: F1yreD
# 2025年12月27日10时22分11秒

class Person:
    # 封装属性（数据）
    def __init__(self, name, age):
        self.name = name  # 姓名属性
        self.age = age  # 年龄属性

    def get_info(self):
        print(f'{self.name} {self.age}')

    def grow_up(self):
        self.age += 1


if __name__ == '__main__':
    zhangsan = Person('张三', 20)
    zhangsan.grow_up()
    zhangsan.age += 1 #类外面可以访问
    zhangsan.get_info()
