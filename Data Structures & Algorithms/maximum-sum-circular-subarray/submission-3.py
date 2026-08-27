class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        currMax, currMin, total = 0, 0, 0

        for num in nums:
            currMax = max(currMax + num, num)
            maxSum = max(maxSum, currMax)
            currMin = min(currMin + num, num)
            minSum = min(minSum, currMin)
            total += num
        
        if maxSum > 0:
            return max(maxSum, total - minSum)
        else:
            return maxSum