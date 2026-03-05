#week02-3.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)#字串長度
        if N1==0: return True

        i = 0#記得i從0開始
        for k in range(N2):#右邊一個去試
            if s[i] == t[k]:#找到一個左右符合的了
                i += 1#左邊i往右升一級
            if i==N1:
                return True

        return False
