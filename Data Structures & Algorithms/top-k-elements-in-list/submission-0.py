from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        n = len(nums)

        bucket = [[] for _ in range(n+1)]

        for number, count in freq_count.items():
            bucket[count].append(number)

        result = []

        for count in range(n, 0, -1):
            for number in bucket[count]:
                result.append(number)
                if len(result) == k:
                    return result
        
        return result