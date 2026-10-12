class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[]
        s=sorted(nums)
        i=0
        j=1
        while i<n:
            arr.append(s[j])
            arr.append(s[i])
            i+=2
            j+=2
        return arr