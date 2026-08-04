class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # early return 0 if begin in set of wordlist,  or begin = end
        # deque q sotores [word, steps] initiliaze ([beginWord, 1])
        # set visited, initiliaze (beginword)
        # if q is not empty, 
        # poleft, word, steps
        # if word == endword , return steps
        # list of word
        # loop through the list
        # set original is current idx letter of word
        # loop through 26 Eng lowwer case letter
        # if original is not equal to the Eng lowwer case letter
        # replace idx letter to Eng letter
        # join the list which with replaced letter
        # if joined new str not in visited, and in set of wordlist
        # visited append the new str, q stores (new str, steps+1)
        # replace back  Eng letter to original one
        # return 0
        # time: O(m*m + n) space: O(m*m + n) m=len(word), n= len(set(wordlist))

        wordSet = set(wordList)
        if endWord not in wordSet or beginWord == endWord:
            return 0

        visited = set()
        visited.add(beginWord)
        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            word_list = list(word)
            for i in range(len(word)):
                original = word_list[i]

                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch != original:
                        word_list[i] = ch
                        new_word = "".join(word_list)

                        if new_word not in visited and new_word in wordSet:
                            visited.add(new_word)
                            q.append((new_word, steps+1))

                word_list[i] = original  
        
        return 0



