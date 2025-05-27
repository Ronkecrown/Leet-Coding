"""
LeetCode.py contain
"""


class LeetCode:
    def isPalindrome(self, x: int) -> bool:  # task 9
        x = str(x)
        if x[::-1] == x:
            return True
        return False

    def twoSum(self, nums: list, target: int) -> list:  # task 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False
