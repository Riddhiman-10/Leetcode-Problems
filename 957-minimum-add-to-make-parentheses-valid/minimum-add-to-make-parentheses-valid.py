class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        freq_open=0
        freq_closed=0
        for i in s:
            if i=='(':
                freq_open+=1
            elif i==')':
                if freq_open>0:
                    freq_open-=1
                else:
                    freq_closed+=1
        return freq_open+freq_closed