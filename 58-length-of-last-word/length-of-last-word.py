class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        i=-1
        while i>=(-1*len(s)) and s[i]!=" ":
            i-=1
        i+=1
        i*=-1
        return i