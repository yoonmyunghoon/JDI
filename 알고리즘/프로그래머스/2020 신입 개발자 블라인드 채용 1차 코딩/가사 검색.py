class Node:
    def __init__(self, w=""):
        self.word = w
        self.remain_check = {}
        self.cList = {}


class Trie:
    def __init__(self):
        self.root = Node("")

    def create(self, words, reverse=False):
        for word in words:
            if reverse:
                word = word[::-1]
            length = len(word)
            cur_node = self.root
            if length in cur_node.remain_check:
                cur_node.remain_check[length] += 1
            else:
                cur_node.remain_check[length] = 1
            for w in word:
                if w not in cur_node.cList:
                    cur_node.cList[w] = Node(w)
                length -= 1
                cur_node = cur_node.cList[w]
                if length in cur_node.remain_check:
                    cur_node.remain_check[length] += 1
                else:
                    cur_node.remain_check[length] = 1

    def search(self, word, check_length):
        num = 0
        cur_node = self.root
        for w in word:
            if w in cur_node.cList:
                cur_node = cur_node.cList[w]
            else:
                return num
        if check_length in cur_node.remain_check:
            return cur_node.remain_check[check_length]
        else:
            return 0


def solution(words, queries):
    answer = []
    dic = {}
    trie = Trie()
    trie.create(words, False)
    r_trie = Trie()
    r_trie.create(words, True)
    for q in queries:
        if q not in dic:
            if q[0] == '?':
                q1 = q[::-1]
                q_count = q1.count('?')
                q1 = q1.replace('?', '')
                answer.append(r_trie.search(q1, q_count))
            else:
                q_count = q.count('?')
                q1 = q.replace('?', '')
                answer.append(trie.search(q1, q_count))
            dic[q] = answer[-1]
        else:
            answer.append(dic[q])
    return answer


w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q = ["fro??", "????o", "fr???", "fro???", "pro?", "???????"]
print(solution(w, q))