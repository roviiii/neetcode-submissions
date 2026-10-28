class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        returnList=[]

        for i in range(len(nums)):
            leftIndex = i + 1
            rightIndex = len(nums) - 1
            
            if nums[i] > 0:
              break
            
            if i > 0 and nums[i] == nums[i - 1]:
               continue


            while leftIndex < rightIndex:
                total = nums[i] + nums[leftIndex] + nums[rightIndex]

                if total < 0:
                    leftIndex += 1

                elif total > 0:
                    rightIndex -= 1

                else:
                    # found a triplet
                    returnList.append([nums[i], nums[leftIndex], nums[rightIndex]])

                    leftIndex += 1
                    rightIndex -= 1

                    while (leftIndex < rightIndex
                        and nums[leftIndex] == nums[leftIndex - 1]):
                        
                        leftIndex += 1



        return returnList
                        