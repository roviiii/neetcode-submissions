class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence=0
        numsSet=set(nums)
        for index in range(len(nums)):
            if nums[index]-1 not in numsSet:
                nextNumber= nums[index]+1
                currentSequence=1
                while nextNumber in numsSet:
                 numsSet.remove(nextNumber)
                 currentSequence+=1
                 nextNumber+=1
                 
                if currentSequence>longestSequence:
                    longestSequence=currentSequence


        return longestSequence
                    
