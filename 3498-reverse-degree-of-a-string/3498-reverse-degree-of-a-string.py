class Solution:
    def reverseDegree(self, s: str) -> int:
        b = list(s)
        sum = 0
        for i in range(len(b)):
            value = 26 - (ord(b[i]) - ord('a'))
            sum += value * (i+1)
        return sum
        