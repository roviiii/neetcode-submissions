class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=[0]*len(nums)
        
        prefix=1
        for index in range(len(nums)):
            product[index]=prefix
            prefix*=nums[index]
        
        postfix=1
        for index in reversed(range(len(nums))):
            product[index]*=postfix
            postfix*=nums[index]

        return product


            
        