class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_num = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i ==0:
                sum_num[i] = nums[i]
            else:
                sum_num[i] = sum_num[i-1]+nums[i]
        return sum_num



