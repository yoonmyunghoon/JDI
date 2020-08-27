
def cal(num):
    result = num
    snum = str(num)
    for i in range(len(snum)):
        result += int(snum[i])
    return result


Max = 10000
check = [1]*(Max+1)
for i in range(1, Max+1):
    c = cal(i)
    if c <= Max:
        check[c] = 0
for i in range(1, len(check)):
    if check[i] == 1:
        print(i)

