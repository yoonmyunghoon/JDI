def countPerms(n):
    # Write your code here
    if n == 0:
        return 0
    elif n == 1:
        return 5
    else:
        data = [1] * 5
        for i in range(1, n):
            a_ = data[1]+data[2]+data[4]
            e_ = data[0]+data[2]
            i_ = data[1]+data[3]
            o_ = data[2]
            u_ = data[2]+data[3]
            data = [a_, e_, i_, o_, u_]
        return sum(data)%(10**9+7)