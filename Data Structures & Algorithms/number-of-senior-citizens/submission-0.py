class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for ele in details:
            cur = ''
            cur +=ele[-4]+ele[-3]
            age = int(cur)
            if age>60:
                result +=1
        return result
        