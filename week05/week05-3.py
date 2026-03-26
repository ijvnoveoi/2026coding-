#week05-3.py
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()
        for c in counter:
            #print(c, counter[c])
            if counter[c] in s:
                return False
            s.add( counter[c] )

        return True
