class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect cycle using Floyd's Algorithm
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Step 2: Find the entrance of the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow  # The duplicate number
