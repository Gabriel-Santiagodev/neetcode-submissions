class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for number in nums:
            hashmap[number] = hashmap.get(number, 0) + 1
        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        return list(hashmap.keys())[:k]


        