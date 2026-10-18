class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=[[] for _ in range(len(nums)+1)]
        frequencyHashMap={}
        returnList=[]
        
        for number in nums:
            frequencyHashMap[number]=frequencyHashMap.get(number,0)+1

        for number in frequencyHashMap:
            frequency[frequencyHashMap[number]].append(number)

        for index in reversed(range(len(nums)+1)):
            for number in frequency[index]:
                if len(returnList)==k:
                    return returnList

                returnList.append(number)


        return returnList
        
        