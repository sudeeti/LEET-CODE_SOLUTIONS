class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(nums, target):
            l, r = 0, len(nums) - 1
            res = -1
            while (l<=r):
                mid = (l + r)//2
                if nums[mid] >= target:
                    r = mid-1
                else:
                    l = mid+1
                if nums[mid]==target:
                    res = mid
            return res

        def right(nums, target):
            l, r = 0, len(nums)-1
            res = -1
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
                if nums[mid] == target:
                    res = mid
            return res
        return [left(nums,target), right(nums,target)] 

                               
