class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            # reading char and calculate the count of same chars
            while read < n and chars[read] == char:
                read += 1
                count += 1
            # write char
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
            


        