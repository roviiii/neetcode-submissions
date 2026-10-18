class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap={}
        for index in range(len(nums)):
            hashMap[nums[index]]=index


        for index in range(len(nums)):
           difference= target- nums[index]
           if difference in hashMap:
             if hashMap[difference]!=index:

                return [ min(hashMap[difference],index),max(hashMap[difference],index)]
          
