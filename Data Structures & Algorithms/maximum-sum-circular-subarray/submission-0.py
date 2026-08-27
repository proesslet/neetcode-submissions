class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]

        currSum = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums) + i):
                currSum += nums[j % len(nums)]
                maxSum = max(currSum, maxSum)
        
        return maxSum