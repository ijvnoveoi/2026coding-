#week02-2.py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)#陣列的大小
        k = 0 #要宣告k
        for i in range(N):#把nums[i]逐一檢查
            if nums[i] != 0:#不是0的到左邊
                nums[k] = nums[i]
                k += 1#換位子

        for i in range(k, N):#剩下的格子
            nums[i] = 0#全部補0
