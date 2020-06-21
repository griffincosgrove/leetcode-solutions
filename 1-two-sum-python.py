class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return_list = []
        hash_map = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in hash_map:
                complement = target - nums[i]
                return_list.append(hash_map[complement])
                return_list.append(i)
            hash_map[nums[i]] = i
        return return_list