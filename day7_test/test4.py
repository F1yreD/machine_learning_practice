# F1yreD
# 2026/1/9 下午8:50
import re

if __name__ == '__main__':
    s1 = ['123@gmail.com',
          '@@asd@gmail.com.cc',
          '431@qq.com']
    pat = r"^\w+@\w+\.\w+$"
    for s in s1:
        match = re.match(pat, s)
        print(f"{s}:{match is not None}")
