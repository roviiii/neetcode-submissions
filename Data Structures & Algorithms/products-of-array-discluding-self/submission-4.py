class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productLeft=[0]*len(nums)
        
        leftProduct = 1 
        for index in range(len(nums)):

            if index!=0:
             leftProduct*= nums[index-1]
            productLeft[index]=leftProduct
        
        
        rightProduct=1
        for index in reversed(range(len(nums))):
            if index != len(nums)-1:
             rightProduct*= nums[index+1]
            productLeft[index]*=rightProduct

        return productLeft
        

        