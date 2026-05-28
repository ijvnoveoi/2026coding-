#week14-2b.py
class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0, 1, 1]
        @cache
        def helper(i):
            if i<3: return a[i]
            return helper(i-1) + helper(i-2) + helper(i-3)
        return helper(n)
