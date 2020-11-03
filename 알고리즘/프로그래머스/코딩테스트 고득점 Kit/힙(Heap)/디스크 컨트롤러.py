import heapq


def solution(jobs):
    pre = []
    heapq.heapify(pre)
    jobs.sort()
    length = len(jobs)
    time = jobs[0][1] + jobs[0][0]
    total = jobs[0][1]
    idx_check = 0
    cnt = 1
    while cnt < length:
        for i in range(idx_check+1, length):
            if time > jobs[i][0]:
                idx_check = i
                heapq.heappush(pre, [jobs[i][1], jobs[i][0]])
            else:
                if pre:
                    break
                else:
                    idx_check = i
                    heapq.heappush(pre, [jobs[i][1], jobs[i][0]])
                    break
        if pre:
            process, start = heapq.heappop(pre)
            if start > time:
                time = start + process
            else:
                time += process
            total += (time - start)
            cnt += 1

    return total//length


ex_jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]
print(solution(ex_jobs))