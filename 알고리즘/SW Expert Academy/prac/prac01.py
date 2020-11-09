import sys
import math
import datetime
import sys
# a = 3.5 - 3.12
# b = 0.38
# c = abs(a - b) <= sys.float_info.epsilon
# c = math.isclose(a,b)
# print(c)

# a = 3
# b = 4
# print(type(a))
# print(a.imag)
# print(a.real)
# print(a.conjugate())

# print('asdf', end='\0')
# print('asdf', end='\t')
# print('asdf', end='\n')
# print('edfafagaff', end='\r')
# print('    ', end='\n')

# print('이 다음은 엔터. \n그리고 탭\t탭 %s %d' %a%b)
# today = datetime.datetime.now()
# print('오늘은 {0:%y}년, {0:%m}월, {0:%d}일입니다.'.format(today))
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(f'{divmod(5, 2)[0]}')
# a= 257
# b=257
# print(a is b)
# print(True + 4)
# print(False + 7)
# int_number = 3
# float_number = 5.8
# complex_number = 3 + 5j
# print(type(int_number+float_number))
# print(type(float_number+complex_number))
# print(type(int_number + complex_number))
# print(int(float_number))
# print(list(range(4, 50)))
# r = list(range(31))
# t = r[0:len(r):3]
# s = list(range(0, 31, 3))
# print(len(r))
# print(t)
# print(s)
# list_a = [1, 2, 3, 1, 1, 2]
# set_a = set(list_a)
# print(set_a)
# print(list_a)
# print(list_a.sort())
a = {1, 5, 6, 8, 4, 5, 6}
# a.sort()
# print(a)
# b = sorted(a)
# print(b)
# print(b.reverse())
# c = reversed(b)
# print(type(c))
# print(3/6 == 0.5)
# a = ['d', 'ds', 'qwer']
# b=''.join(a)
# print(type(b))
# print(a)
# print(list(enumerate(a, start=2)))
# a = 10
# def bbbb():
#     a = 4
#     print(a)


# bbbb()
# print(a)

# v = sys.maxsize
# print(v+1)
# print(a.discard(9))
# my_account = {
#     'username': '홍길동',
#     'password': '1q2w3e4r',
#     'password_confirmation': '1q2w3e4r'
# }
# def signup(username, password, password_confirmation):
#     print(username)
#     print(password)
#     if password == password_confirmation:
#         print(f'{username}님, 환영합니다.')
#     else:
#         print(f'비밀번호가 일치하지 않습니다.')

# signup(**my_account)


# print(('a', 'd')+('v', 'ds'))
# from math import pi

# x = 10
# y = 11
# def foo():
#     x = 20
#     def bar():
#         a = 30
#         print(a, x, y, pi)
#     bar()
#     x = 40
#     bar()

# foo()

# a = {1:1, 5:2, 4:5}
# a.update({'귤','토마토'})
# print(a.pop('사과'))
# print(a)
words = "hI! Everyone, I'm kim"
# words.capitalize()
# result = words.title()
# result = words.upper()
# print(result)
# print('woooooowooo'.replace('o', '', 2))
# print('Hi! jussssstin'.replace('s', ''))


# a = 'Hello, World'
# print(a.istitle())
# b = 'Hello, world'
# print(b.title())
# print(b.istitle())
# print(b)
# L = [1, 2, 3]
# S = L + [4] # 새로운 리스트를 만듦
# print(L)
# print(S)
# L.append(4) # 기존 리스트의 마지막에 추가
# print(L)

# def even(n):
#     if n%2 == 0:
#         return n
# numbers = [1, 2, 3, 4, 5, 2, 2]
# n= list(filter(even, numbers))
# print(n)
# result = [number for number in numbers if even(number)]
# print(result)

# a=1
# b=5
# def adddd():
#     a = 7
#     return a+b

# print(adddd())
# power = False
# number = ''
# book = {}
# model = 'LG V10'

# # 핸드폰이 할 수 있는 행위(행동)
# def on():
# #     global power
#     if not power: # 핸드폰이 꺼져있다면
#         power = True # 전원을 키자
#         return power
# def off():
# #     global power
#     if power: # 핸드폰이 켜져있다면
#         power = False # 전원을 끄자
#         return power
# def set_my_number(number):
#     if power: # 핸드폰 전원이 켜져있으면
#         number = number # 내 전화번호 설정
# def call(number):
#     if power: # 핸드폰 전원이 켜져있으면
#         if number in book: # 인자로 받은 전화번호가 전화번호부에 있다면
#             print('{} 에게 전화를 걸고 있습니다...'.format(book[number])) # 그 사람에게 전화
#         else: # 인자로 받은 전화번호가 전화번호부에 없다면
#             print('{}로 전화를 걸고 있습니다...'.format(number)) # 그냥 그 번호로 전화
# def save(name, number):
#     if power: # 핸드폰이 켜져있다면
#         book[name] = number # 전화번호 추가
#         return book

# save('엄마', '01048036265')

class Phone:
    power = False
    number = ''
    book = {}
    model = 'LG V10'
    
    def on(self):
        if not self.power:
            self.power = True
            print('--------------')
            print(f'{self.model}')
            print('--------------')
    
    def off(self):
        if self.power:
            self.power = False
            print('폰 꺼짐')

p = Phone() # 인스턴스(p) 객체 생성
print(p.model)
reynold_phone = Phone()
print(reynold_phone.power)
reynold_phone.on()
print(reynold_phone.power)
print(isinstance(reynold_phone, Phone))
print(type(reynold_phone) == Phone)
print(type(reynold_phone))
print(reynold_phone)
