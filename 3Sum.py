class Solution(object):
    def threeSum(self, nums: list) -> list:
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]*-1
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    inst = Solution()
    res = inst.threeSum(nums)
    print(res)