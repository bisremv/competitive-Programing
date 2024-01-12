from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to make it easier to find unique quadruplets
        result = []
        n = len(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                left, right = j + 1, n - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        temp=[nums[i], nums[j], nums[left], nums[right]]
                        temp.sort()
                        if temp not in result:
                            result.append(temp)

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result
