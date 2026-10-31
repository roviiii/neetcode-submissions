class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSequence=0
        hashSet=set(nums)
        currentSequence=1

        for number in hashSet:
           currentSequence=1
            
           if number-1 not in hashSet:
            currentNumber=number
            while currentNumber+1 in hashSet:
                currentSequence+=1
                currentNumber+=1

            

            if currentSequence> longestSequence:
                longestSequence=currentSequence
            

           
           

        
        return longestSequence
        