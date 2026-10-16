class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #list where the index is the sequence length and the value is the list of numbers 
        sequenceList=[[]for _ in range(len(nums))]
        longestSequence=0
        seen=set()
        

        for number in nums:
            seen.add(number)
        #loop through values in seen then check if for loop agai +1 is still a thing if it is add it to 
        #the sequnce list then also remove the number from the seen set()
        for index in range(len(nums)):

            if nums[index] not in seen:
                continue
            sequenceNumber = 1
            if nums[index] - sequenceNumber not in seen:
                seen.remove(nums[index])
                while nums[index] + sequenceNumber in seen:
                    seen.remove(nums[index] + sequenceNumber)
                    sequenceNumber += 1
                if sequenceNumber > longestSequence:
                    longestSequence=sequenceNumber
 
 

        return longestSequence
            
