
def solution(array, commands):
    result = []
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        new_array.sort()
        result.append(new_array[commands[i][2]-1])
    return result


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))