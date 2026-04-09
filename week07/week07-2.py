#week07-2.py
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a>0:#正的往右, 不會跟左邊相撞
                ans.append(a)#直接塞()
            else:#負的往左
                while ans and ans[-1]>0:
                    if abs(ans[-1]) == abs(a):
                        ans.pop()
                        a = 0
                        break
                    elif abs(ans[-1]) > abs(a):
                        a = 0
                        break
                    else:
                        ans.pop()
                if a != 0: ans.append(a)
        return ans
