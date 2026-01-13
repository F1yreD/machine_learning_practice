# F1yreD
# 2026/1/11 上午11:32
import random


class RandArr:
    def __init__(self, length):
        self.length = length
        self.arr = []
        self.__rand_num()

    def __rand_num(self):
        for i in range(self.length):
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


if __name__ == '__main__':
    q = RandArr(10)
    print(q.arr)
    quick_sort(q.arr, 0, len(q.arr) - 1)
    print(q.arr)
