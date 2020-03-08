from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter()
        for word in nums:
            c[word] += 1
        c = dict(c)
        return(list(c.keys())[list(c.values()).index(1)])
