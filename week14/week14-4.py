#week14-4.py
from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def helper(i):
            if i >= len(nums):
                return 0

            return nums[i] + max(helper(i+2), helper(i+3))

        return max(helper(0), helper(1))

