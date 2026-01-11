
def print_hello():
    i = 0
    while i < 5:
        print('hello world')
        i += 1  # 循环内必须有让判断条件趋近于假


def daffodils():
    """
    求水仙花数
    :return:
    """
    num = 100
    while num <= 999:
        a = num % 10
        b = num // 10 % 10
        c = num // 100
        if a ** 3 + b ** 3 + c ** 3 == num:
            print(num)
        num += 1


def use_for():
    my_list = [1, 2, 3, 4, 8]
    for i in my_list:
        print(i, end=' ')


def use_for_str():
    for i in '今天天气很好，所以心情好':
        if i == '好':
            print(i, end=' ')


def use_range():
    """
    range是左闭右开，默认从0开始
    :return:
    """
    for i in range(10, 0, -2):
        print(i, end=' ')


def use_two_while():
    """
    循环嵌套
    外层控制多少行，内层控制多少列
    :return:
    """
    i = 0
    while i < 5:
        j = 0
        while j < 8:
            print('*', end='')
            j += 1
        print()
        i += 1


def print_triangle():
    """
    打印三角形
    :return:
    """
    i = 1
    while i <= 5:
        j = 0
        while j < i:
            print('*', end='')
            j += 1
        print()
        i += 1


def use_break():
    for i in range(1, 6):
        if i==4:
            print('吃饱了')
            break
        print(f'我吃了{i}号苹果')

def use_continue():
    for i in range(1, 6):
        if i==4:
            print('有虫子，我不吃这个苹果')
            continue
        print(f'我吃了{i}号苹果')
# print_hello()
# daffodils()
# use_for()
# use_for_str()
# use_range()
# use_two_while()
# print_triangle()
# use_break()
use_continue()