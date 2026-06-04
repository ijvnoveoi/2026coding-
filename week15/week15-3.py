#week15-3.py
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @cache
        def helper(i, hasStock):  # 紀錄第 i 天是否有 hasStock 股票?

            if i == len(prices):
                return 0  # 終止條件

            # 只有兩種，可以賣? 買? 或持有?
            if hasStock:
                ans = prices[i] + helper(i+1, False) - fee  # 賣掉後 fee，得到錢 prices[i]
            else:
                ans = -prices[i] + helper(i+1, True)  # 花了錢 prices[i]，得到股票

            # 不買、不賣
            ans = max(ans, helper(i+1, hasStock))  # 比較相同，直接撐下一天

            return ans

        return helper(0, False)  # 第 0 天開始選擇，手上沒有股票
