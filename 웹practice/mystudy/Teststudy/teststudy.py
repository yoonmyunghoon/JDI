# a = ['d', 's', 'a']
# b = ''.join(a)
# print(b)

# c = {1,2,3,4}
# d = {4,5,6,7,8}

# print(c & d)

# a = [1,2,3,4,5,5,5,5,7]
# b = set(a)
# a = list(b)
# print(a)

# phone_book = {'서울': '02', '경기': '031', '인청': '032'}
# print(phone_book.items())

# for i in range(2, 10):
#     print('{}단'.format(i))
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i*j}')

# word = input()
# vowels = 0
# consonants = 0
# for i in word:
#     if i in 'aeiou':
#         vowels += 1
#     else:
#         consonants += 1
# print(vowels, consonants)

# classroom = ['Kim', 'Hong', 'kang']
# print(list(enumerate(classroom, start=1)))

# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
# fruit_num = 0
# fruit_numx = 0
# for k, v in basket_items.items():
#     if k in fruits:
#         fruit_num += v
#     else:
#         fruit_numx += v
# print(fruit_num, fruit_numx)

# city = {
#     '서울': [-6, -10, 5],
#     '대전': [-3, -5, 2],
#     '광주': [0, -2, 10],
#     '부산': [2, -2, 9],
# }

# cold = 0
# hot = 0
# count = 0
# hot_city = ""
# cold_city = ""

# for k, v in city.items():
#     if max(v) > hot:
#         hot = max(v)
#         hot_city = k
#     if min(v) < cold:
#         cold = min(v)
#         cold_city = k

# print(hot, hot_city, cold, cold_city)

# words = "hI! Everyone, I'm kim"
# print(words.swapcase())
# print('woooooowooo'.replace('o', '', 2))
# caffe = ['starbucks', 'tomntoms', 'hollys']
# caffe.append(['asfds'])
# caffe.extend(['adasfd'])
# print(caffe)
# print(dir(list))
# numbers = [2, 5, 4, 1, 7, 5]
# result = sorted(numbers, reverse=True)
# numbers.sort(reverse=True)
# print(result) # return값
# print(numbers) # 원본
# import random

# a = random.sample(numbers, 2)
# print(a)

my_dict = {'apple': '사과', 'banana': '바나나'}
a= my_dict.get('melon', True)
print(a)
