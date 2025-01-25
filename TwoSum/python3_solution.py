from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        最直接想是
        for first_num in nums:
            for second_num in nums:
                不相同則相加看看是不是等於target
                    
        要注意時間複雜度 <= O(n2)
        
        那就表示要用空間換時間
        -> 跑第一次for loop 要記錄某一些結果, 避免第二次for loop
        
        a + b = target
        b = target - a
        我只要每次都存a 接著去找找看b有沒有出現過這樣應該就可以只跑一個 for loop
        """
        
        result = {}
        
        for idx, num in enumerate(nums):
            if (diff_num := target - num) in result:
                return [result[diff_num], idx]
                
            result[num] = idx
            

example_params = [
    {
        "nums": [2, 7, 11, 15],
        "target": 9,
        "answer": [0, 1]
    },
    {
        "nums": [3, 2, 4],
        "target": 6,
        "answer": [1, 2]
    },
    {
        "nums": [3, 3],
        "target": 6,
        "answer": [0,1]
    },
]

solution = Solution()
for params in example_params:
    answer = params.pop("answer", None)
    result = solution.twoSum(**params)
    
    try:
        assert answer == result
        print("\033[92m pass! \033[0m")
    except AssertionError:
        print(f"\033[91m {answer=}\t{result=} \033[0m")
