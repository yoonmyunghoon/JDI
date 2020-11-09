
# 진수변환 다른 진법 수를 10진수로 바꿔줌
print(int("1002", 3))

# 문자열 함수들
name = "reynold"
print("hi, i'm {}".format(name))
introduce = ["hi", "i'm", "reynold"]
print(" ".join(introduce))
alphabet = "abcd"
print(",".join(alphabet))
ex_strip = "    s    "
print(ex_strip.strip())
a = "hobby"
print(a.count("b"))
print(a.find("b"))
print(a.find("c"))
print(a.index("b"))
# print(a.index("c"))  # 오류
ex_split = "Life is too short"
print(ex_split.split())

# 리스트
import copy
list1 = [[1, 2, 3], [2, 3]]
list2 = list1[:]
list1.append(1)
print(list1)
print(list2)
list1[0].append(4)
print(list1)
print(list2)
list3 = copy.deepcopy(list1)
list1[0].append(5)
print(list1)
print(list3)

list4 = [3, 4, 1, 5, 23, 51, 55, 2, 4, 32, 12, 13]
list4.sort()
print(list4)
list5 = [(2, 6), (1, 4), (3, 4), (4, 5)]
list5.sort(key=lambda x: (-x[1], x[0]))
print(list5)
list6 = [(2, 'cb'), (1, 'bb'), (3, 'bb'), (4, 'ab')]
list6.sort(key=lambda x: (x[1], -x[0]), reverse=True)
print(list6)

# 튜플 - 내부의 값을 변환할 수 없음

# 딕셔너리 - dic.keys(), dic.values(), dic.items()

# set - 중복x, 순서x, |(합집합), &(교집합), -(차집합), ^(합집합-교집합)
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
c = {4, 5, 6}
print(b.issubset(a))
print(a.issuperset(b))
print(c.isdisjoint(b))





