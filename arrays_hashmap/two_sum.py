class Solution:
    def twoSum(self, nums, target: int):
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

if __name__=='__main__':
    sol=Solution()
    lst=sol.twoSum([2,7,1,3],9)
    print(lst)