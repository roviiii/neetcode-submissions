class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        productRight = {}
        productLeft = {}
        returnList = []

        indexList = range(len(nums))

        currentProduct = 1

        for index in indexList:
            productRight[index] = currentProduct
            currentProduct *= nums[index]

        currentProduct = 1

        for index in reversed(indexList):
            productLeft[index] = currentProduct
            currentProduct *= nums[index]

        for index in indexList:
            returnList.append(
                productLeft[index] * productRight[index]
            )

        return returnList

