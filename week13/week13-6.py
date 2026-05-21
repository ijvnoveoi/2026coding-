#week13-6.py

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)   # 得到長度
        a = [(nums2[i], nums1[i]) for i in range(n)]  # 左右合併起來
        #print(a)
        # a.sort()   # 排序寫法：小到大排序
        #print(a)
        a.sort(reverse=True)   # 大到小排序
        heap = [a[i][1] for i in range(k)]
        heapify(heap)   # 之後都會從 nums1 的 k 個值，換入新的 n1,n2 組
        total = sum(heap)
        ans = total * a[k-1][0]   # 前 k 項的 nums1 和乘最小的 nums2
        for i in range(k, len(nums2)):   # 後面再加入的數
            n2, n1 = a[i]   # 把加入的新數值取出
            heappush(heap, n1)   # 加入
            total += n1 - heappop(heap)   # 加入，扣掉最小值
            ans = max(ans, total * n2)   # 更新答案
        return ans
