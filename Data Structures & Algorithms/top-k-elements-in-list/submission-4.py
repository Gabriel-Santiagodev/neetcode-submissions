from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = Counter(nums)
        sorted_dict_desc = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict_desc)[:k]       