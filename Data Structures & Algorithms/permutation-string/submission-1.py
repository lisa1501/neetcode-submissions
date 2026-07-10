class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = Counter()
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            char = s2[r]
            count_s2[char] += 1

            if r - l + 1 > k:
                left_char = s2[l]
                count_s2[left_char] -= 1
                l += 1
        
                if count_s2[left_char] == 0:
                    del count_s2[left_char]

            if count_s1 == count_s2:
                return True

        return False