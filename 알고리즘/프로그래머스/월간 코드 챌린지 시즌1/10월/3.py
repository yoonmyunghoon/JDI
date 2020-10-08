def solution(n, edges):
    answer = 0
    check_box = [0]*(n+1)
    tree = {}
    for e in edges:
        check_box[e[0]] += 1
        check_box[e[1]] += 1
        if e[0] in tree:
            tree[e[0]].append(e[1])
        else:
            tree[e[0]] = [e[1]]
        if e[1] in tree:
            tree[e[1]].append(e[0])
        else:
            tree[e[1]] = [e[0]]
    print(tree)
    print(check_box)

    return answer

N = 5
Edges = [[1,5],[2,5],[3,5],[4,5]]
print(solution(N, Edges))