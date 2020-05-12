def solution(n, path, order):
    tmpl = [0 for _ in range(n)]
    tmpl3 = [0 for _ in range(n)]
    d = [[] for _ in range(n)]
    for a, b in path:
        d[a].append(b)
        d[b].append(a)
    nl = [-1 for _ in range(n)]
    for b, a in order:
        nl[b] = a
        tmpl[a] = 1
        tmpl3[b] = 1
    tmplcnt = sum(tmpl)
    for i in range(n):
        if not tmpl[i]:
            tmpl1 = tmpl.copy()
            tmpl2 = tmpl3.copy()
            tmpl1cnt = tmplcnt
            # 각 점에서 시작해서 bfs한다
            # 먼저밟아야하는걸 밟았으면 bfs 한번더 할 수 있다.
            # 없었으면 끝낸다.
            chkset = set()
            chklist = []
            st = [i]
            vl = [0 for _ in range(n)]
            vl[i] = 1
            while st:
                idx = st.pop()
                for nextnode in d[idx]:
                    if not tmpl1[nextnode]:
                        # 방문할수 있는 곳이면
                        if not vl[nextnode]:
                            st.append(nextnode)
                            vl[nextnode] = 1
                            if tmpl2[nextnode]:
                                # 갱신할 수 있다면
                                if tmpl1[nl[nextnode]]:
                                    chklist.append(nl[nextnode])
                                    tmpl1[nl[nextnode]] = 0
                                    tmpl1cnt -= 1
                                tmpl2[nextnode] = 0
                    else:
                        chkset.add(nextnode)

                while chklist:
                    nextnode = chklist.pop()
                    if nextnode in chkset:
                        vl[nextnode] = 1
                        st.append(nextnode)
            if not tmpl1cnt:
                # 모두 방문할 수 있다면
                return True
    return False

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))