class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            suum=0
            stnum= str(nums[i])
            for c in stnum:
                suum+=int(c)
            if suum==i:
                return i
        else:
            return -1                