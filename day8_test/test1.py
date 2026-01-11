# csr
# 2026/1/11 下午8:05
# 1
import re

if __name__ == '__main__':
    s = "123@qq.com 567@qq.com"
    pat1 = r"\d*3@qq.com"
    pat2 = r"qq"
    pat3 = r'\s'
    res1 = re.search(pat1, s)
    res2 = re.findall(pat1, s)
    res3 = re.sub(pat2, 'gmail', s)
    res4 = re.split(pat3, s)
    if res1:
        print("search:", res1.group(), res1.span())
    if res2:
        print("findall:", res2)
    print(res3)
    print(res4)
