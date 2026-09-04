class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # take mid
        # if mid is not target, check if left < target < mid 
        # if left < target < mid, go left
        # else (if left > target OR target > mid, go right)
        l = 0
        r = len(nums) - 1
        # curMin = nums[l]
        while l <= r:
            mid = l + (r-l) // 2
            # curMin = min(nums[mid], curMin)
            #print(f"current mid: {mid}")
            if nums[mid] == target:
                return mid
            
            # check what portion of the sort we are in
            if nums[l] <= nums[mid]:
                # we are in the sorted right
                # now. target could be l - mid, mid - pivot, pivot - r
                if target < nums[l]: # pivot - r, go right
                    l = mid + 1
                else: # now target could be in l - mid, mid - pivot
                    if target < nums[mid]: # l - mid, go left
                        r = mid - 1
                    else: # mid - pivot, go right
                        l = mid + 1

            else:
                # we are in the sorted left
                # if target is greater than right, 
                # then we go left
                if target > nums[r]: #target must be in l - pivot
                    r = mid - 1
                else: # now, target could be in l - pivot, pivot - mid, mid - r
                    if target > nums[mid]: # mid - r
                        # search right
                        l = mid + 1
                    else: # pivot - mid
                        # search left
                        r = mid - 1

            # if nums[l] <= target and target < nums[mid]:
            #     #go left
            #     r = mid - 1
            # else:
            #     #go right
            #     l = mid + 1
        return -1