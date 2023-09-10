import numpy as np
from typing import List

class Solution:
    def moveZeroes_Zhao(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        nums_non0 = [num for num in nums if num != 0]
        size_pad = size - len(nums_non0)
        nums[:] = nums_non0 + [0] * size_pad
    
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

    
if __name__ == '__main__':
    test = Solution()
    nums = [0,1,0,3,12]
    test.moveZeroes(nums)
    print(nums)