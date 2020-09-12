def check(c_node, words, d):
    if d == 4:
        num = 0
        for score in c_node.cList:
            if int(score) >= int(words[4]):
                num += 1
        return num
    if words[d] == '-':
        num = 0
        for child in c_node.cList:
            num += check(c_node.cList[child], words, d + 1)
        return num
    else:
        if words[d] in c_node.cList:
            return check(c_node.cList[words[d]], words, d + 1)
        else:
            return 0


class Node:
    def __init__(self, w=""):
        self.word = w
        self.cList = {}
        self.dept = -1


class Trie:
    def __init__(self):
        self.root = Node("")

    def create(self, words):
        words = list(words.split(' '))
        cur_node = self.root
        num = -1
        for word in words:
            if word not in cur_node.cList:
                cur_node.cList[word] = Node(word)
            num += 1
            cur_node.dept = num
            cur_node = cur_node.cList[word]

    def search(self, words):
        cur_node = self.root
        return check(cur_node, words, 0)


def solution(info, query):
    answer = []
    trie = Trie()
    for a_info in info:
        trie.create(a_info)
    for a_query in query:
        a_query = a_query.replace('and ', '')
        a_query = list(a_query.split(' '))
        answer.append(trie.search(a_query))
    return answer


Info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
Query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(Info, Query))
