#week15-2b.py
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)  # 兩字串的長度
        table = [[0] * (N + 1) for i in range(M + 1)]
        for i in range(M):
            for j in range(N):
                # case1 = table[i-1][j]  往上面
                # case2 = table[i][j-1]  往左邊
                # case3 = table[i-1][j-1] + 1  若左上角（遇到相同，左上角 + 1）
                if text1[i] == text2[j]:
                    table[i+1][j+1] = table[i][j] + 1
                table[i+1][j+1] = max(
                    table[i+1][j+1],
                    table[i+1][j],
                    table[i][j+1]
                )
        return table[M][N]
