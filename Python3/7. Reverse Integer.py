class Solution:
    def reverse(self, x: int) -> int:
        c = []
        for digit in str(x):
            c.append(digit)
        if c[0] == '-':
            del c[0]
            c.insert(len(c), '-')
        num = int(''.join(map(str, c[::-1])))
        if abs(num) > 2**31:
            return 0
        else:
            return num
