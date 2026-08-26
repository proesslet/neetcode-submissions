class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        sortedCounts = []
        for num, count in counts.items():
            sortedCounts.append([count, num])
        sortedCounts.sort()

        result = []
        while len(result) < k:
            result.append(sortedCounts.pop()[1])
        return result