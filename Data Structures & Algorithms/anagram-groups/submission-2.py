class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize a hashmap
        # for loop strs
        # initialize a list [0]*26
        #  for loop str in strs
        #  increase list element by ord of ch
        # if list not in hashmap, store list as a key, value as [str]
        # else hashmap key append str
        # return all values in hashmap in a list
        # Time:O(n*m) n len(strs) m len(str)
        # Space: O(n*m)

        freq = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1

            freq[tuple(count)].append(s)
        
        return [val for val in freq.values()]     