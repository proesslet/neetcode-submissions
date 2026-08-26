class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        ones = 0
        index = 0
        while index < len(nums):
            if (nums[index] == 1):
                ones = ones + 1
                if (ones > maxOnes):
                    maxOnes = ones
            else:
                if (ones > maxOnes):
                    maxOnes = ones
                ones = 0
            index += 1
        return maxOnes