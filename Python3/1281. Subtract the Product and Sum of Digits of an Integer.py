import numpy as np
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        c = []
        for digit in str(n):
            c.append(int(digit))
        return(np.prod(c) - np.sum(c))
