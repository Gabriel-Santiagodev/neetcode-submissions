from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = Counter(nums)
        result = []
        for i in lst.most_common(k):
            result.append(i[0])
        return result
        