class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums)):

            if nums[i] > 0: # no negative numbers in the list, hence cannot get 0
                break
            
            if i > 0 and nums[i] == nums[i-1]: # if same as previous number, skip
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0: # sum too big reduce bigger number
                    r -= 1
                elif threeSum < 0: # sum too small increase smaller number
                    l += 1
                else: # sum == 0
                    results.append([nums[i], nums[l], nums[r]]) 
                    l += 1 # continue search
                    r -= 1 # continue search
                    while nums[l] == nums[l-1] and l<r: # if left: consecutive numebers are the same go to next
                        l+=1
        return results



