class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[]for _ in range(len(nums)+1)]
        hashMap={}
        returnList=[]
        # key is number and value is the frequency
        for number in nums:
            hashMap[number]=hashMap.get(number,0)+1
        
        for number in hashMap:
            bucket[hashMap[number]].append(number)
        
        for index in reversed(range(len(bucket))):
            for number in bucket[index]:
                returnList.append(number)

                if len(returnList)== k:
                    return returnList 
                
            


        