class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[l]
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= nums[l]:
                # left portion sorted, search right
                res = min(nums[l], res)
                l = mid + 1
            else:
                # currently is the right sorted portion, search left
                res = min(nums[mid], res)
                r = mid - 1
        return res