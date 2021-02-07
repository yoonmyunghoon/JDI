import sys
from collections import Counter
sys.stdin = open("2805_나무 자르기.txt")


def find_h(s, e):
    while s <= e:
        h = (s+e)//2
        k = 0
        for tree, cnt in cnt_trees.items():
            if tree > h:
                k += (tree-h)*cnt
        if k == M:
            return h
        elif k < M:
            e = h - 1
        else:
            s = h + 1
    return e


N, M = map(int, input().split())
trees = list(map(int, input().split()))
cnt_trees = Counter(trees)
max_h = max(trees)
print(find_h(0, max_h))
