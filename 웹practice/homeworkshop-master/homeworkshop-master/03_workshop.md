# 03_workshop

## 01_문제

```python
#1 - 1
# a = input()
# def Palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

# print(Palindrome(a))

#1 - 2
a = input()
def is_palindrome(word):
    list_word = list(word)
    for i in range(len(list_word) // 2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
print(is_palindrome(a))


```



