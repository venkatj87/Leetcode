class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        explored_set = {}
        for i, num in enumerate(nums):
            current_number = nums[i]
            lookup = target - current_number
            if (lookup in explored_set):
                return[i, nums.index(lookup)]
            explored_set[num] = i

        return None