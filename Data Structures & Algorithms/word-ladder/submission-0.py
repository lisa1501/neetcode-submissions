class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:

            word, length = queue.popleft()

            if word == endWord:
                return length

            word_chars = list(word)

            for i in range(len(word)):

                original = word_chars[i]

                # Try replacing this character with every letter
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == original:
                        continue

                    word_chars[i] = ch
                    new_word = "".join(word_chars)

                    if (
                        new_word in wordSet
                        and new_word not in visited
                    ):
                        visited.add(new_word)
                        queue.append((new_word, length + 1))

                # Restore original character
                word_chars[i] = original

        return 0
        