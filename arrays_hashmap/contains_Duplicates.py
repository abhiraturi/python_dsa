class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        print(nums)
        return False

if __name__=='__main__':
    sol=Solution()
    value=sol.containsDuplicate([2,7,1,3,3])
    print(value)