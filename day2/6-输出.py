
def use_print1():
    print('hello', end='')  # 输出不想有换行
    print('world')
    print('-' * 50)

    print('hello', end=' ')
    print('world', end=' ')
    print('kaoyan', )

    print('-' * 50)
    print('hello\n\nworld')


def use_print_format():
    """
    使用print的格式化输出
    :return:
    """
    age = 10
    print("我今年%d岁了" % age)

    name = '老天师'
    print("%s, 你败过吗？" % name)

    score = 88.5
    print("我叫蜡笔小新，今天考了%f分" % score)

    print('我叫%s, 我的学号是%5d, 我的成绩是%.3f' % ('张三', 12, 382.58))

    # 插值表达式,重点
    print(f'我叫{name}, 我今年{age:03d}岁了, 在宗门小比中，我得了{score}分')

    print('我叫{},今年{}'.format(name,age))

# use_print1()
use_print_format()
