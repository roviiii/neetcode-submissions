class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        productRight = {}
        productLeft = {}
        returnList = [0]* len(nums)

        indexList = range(len(nums))

        currentProduct = 1

        for index in indexList:
            productRight[index] = currentProduct
            currentProduct *= nums[index]

        currentProduct = 1

        for index in reversed(indexList):
            returnList[index] = currentProduct
            currentProduct *= nums[index]

        for index in indexList:
            returnList[index]*= productRight[index]
            

        return returnList

