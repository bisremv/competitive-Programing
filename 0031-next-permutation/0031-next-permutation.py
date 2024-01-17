from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length_nums = len(nums)

        # Find the first decreasing element from the right
        i = length_nums - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such element is found, find the smallest element to the right of it that is greater
        if i >= 0:
            j = length_nums - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray to the right of i
        left, right = i + 1, length_nums - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
