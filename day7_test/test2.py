# F1yreD
# 2026/1/9 下午6:08
# test2
import os


def dir_scan(path, w):
    all_files = os.listdir(path)
    os.chdir(path)
    for file in all_files:
        print(w * '\t', file)
        if os.path.isdir(file):
            dir_scan(file, w+1)
    os.chdir('..')


if __name__ == '__main__':
    dir_scan('.', 0)