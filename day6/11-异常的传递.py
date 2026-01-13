# 作者: F1yreD
# 2025年12月29日14时08分26秒


def demo1():
    num = int(input('请输入一个整数'))
    print(num)


def demo2():
    demo1()
    print('demo2执行结束')


if __name__ == '__main__':
    try:
        demo2()
    except Exception as e:
        print(e)
