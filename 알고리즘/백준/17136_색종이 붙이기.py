import sys
sys.stdin = open("17136_색종이 붙이기.txt")




paper = [list(map(int, input().split())) for _ in range(10)]
for p in paper:
    print(p)
print()

