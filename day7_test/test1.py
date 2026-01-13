# F1yreD
# 2026/1/9 下午5:59
import os


# test1
def o_f():
    with open("dir/file1.txt", "r") as f:
        print(f.read())


def w_f():
    with open("dir/file1.txt", "w") as f:
        f.write("hello world")


if __name__ == '__main__':
    w_f()
    o_f()
