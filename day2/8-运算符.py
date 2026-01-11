
def use_cal():
    """
    算术运算符
    :return:
    """
    print(5 / 2)
    print(5 // 2)
    print(5 % 2)
    print(2 ** 3)
    a = 1
    a += 1
    print(a)


def use_logic():
    """
    逻辑运算符
    :return:
    """
    print(3 and 5)
    print(3 or False)
    print(not 0)


def use_bit():
    """
    位运算符，只能对整型类型运算
    Python的负数 是以补码形式在内存中存储的
    :return:
    """
    # 5    0000 0101
    # 7    0000 0111
    print(5 & 7)  # 按位与
    print(5 | 7)  # 按位或
    print(~5)
    print(5 << 1)  # 左移 乘2
    print(10 >> 1)  # 右移 正数 除2
    print(-5 >> 1)  # 右移减1除2
    print(5 ^ 7)  # 异或  0000 0010
    print(3 ^ 3)
    print(3 ^ 0)  # 一个数和零异或得到自身


def find_num():
    """
    找出出现一次的那个数
    遍历一次，把只出现一次的数，找出来
    :return:
    """
    my_list = [3, 4, 5, 4, 3]
    result = 0
    for i in my_list:
        result ^= i
    print(result)


def use_ternary():
    """
    三目运算符
    :return:
    """
    a = 8
    b = 5
    print(a if a > b else b)


# use_cal()
# use_logic()
# use_bit()
# find_num()
use_ternary()
