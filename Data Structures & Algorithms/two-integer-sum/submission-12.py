class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for key, value in enumerate(nums):
            result = target - value
            if result in hashmap:
                return [hashmap[result], key]
            hashmap[value] = key
