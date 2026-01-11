# csr
# 2026/1/11 下午8:40
import random


class RandArr:
    def __init__(self, cnt):
        self.cnt = cnt
        self.arr = []
        self.__rand_num()

    def __rand_num(self):
        for i in range(self.cnt):
            self.arr.append(random.randint(0, 99))


def quick_sort(arr, l, r):
    if l >= r:
        return
    i, j, x = l - 1, r + 1, arr[l + r >> 1]
    while i < j:
        while True:
            i += 1
            if arr[i] >= x:
                break
        while True:
            j -= 1
            if arr[j] <= x:
                break
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    quick_sort(arr, l, j), quick_sort(arr, j + 1, r)


def down(u):
    t = u
    if u * 2 + 1 < q.cnt and q.arr[u * 2 + 1] > q.arr[t]:
        t = u * 2 + 1
    if u * 2 + 2 < q.cnt and q.arr[u * 2 + 2] > q.arr[t]:
        t = u * 2 + 2
    if u != t:
        q.arr[u], q.arr[t] = q.arr[t], q.arr[u]
        down(t)


def heap_sort():
    for i in range(q.cnt // 2 - 1, -1, -1):
        down(i)
    for i in range(q.cnt - 1, 0, -1):
        q.arr[0], q.arr[i] = q.arr[i], q.arr[0]
        q.cnt -= 1
        down(0)


if __name__ == '__main__':
    q = RandArr(10)
    print(q.arr)
    quick_sort(q.arr, 0, len(q.arr) - 1)
    print(q.arr)
    q = RandArr(10)
    print(q.arr)
    heap_sort()
    print(q.arr)
