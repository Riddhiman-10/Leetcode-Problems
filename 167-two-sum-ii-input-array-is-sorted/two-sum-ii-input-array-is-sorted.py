class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lt=0
        rt= len(numbers)-1
        while lt<rt:
            sum=numbers[rt]+numbers[lt]
            if sum== target:
                return [lt+1,rt+1]
            elif sum> target:
                rt-=1
            else:
                lt+=1