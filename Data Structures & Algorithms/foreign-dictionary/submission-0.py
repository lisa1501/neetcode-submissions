class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {c:0 for w in words for c in w}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1

                    break
                else:
                    if len(word1) > len(word2):
                        return ""

        q = deque([c for c in indegree if indegree[c] == 0])

        order = []

        while q:
            char = q.popleft()
            order.append(char)

            for nei in graph[char]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)


        if len(order) != len(indegree):
            return ""
        return "".join(order)