class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        重點: 直接記住差值，不用再去重複查找
        """
        diff_num_dict = {}

        for index, num in enumerate(nums):
            diff_num = target - num

            if diff_num in diff_num_dict:
                return [diff_num_dict[diff_num], index]
            else:
                diff_num_dict[num] = index


solution = Solution()

# Example 1: nums = [2,7,11,15], target = 9
assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
print(f"\033[92m Test case 1 passed \033[0m")

# Example 2: nums = [3,2,4], target = 6
assert solution.twoSum([3, 2, 4], 6) == [1, 2]
print(f"\033[92m Test case 2 passed \033[0m")

# Example 3: nums = [3,3], target = 6
assert solution.twoSum([3, 3], 6) == [0, 1]
print(f"\033[92m Test case 3 passed \033[0m")
