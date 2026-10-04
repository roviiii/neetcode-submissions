class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequant_Number_in_order=[]
        frequency={}
        
        
        buckets = [[] for _ in range(len(nums) + 1)]

        if len(nums) == 0 :
            return most_frequant_Number_in_order

        for number in nums:
            frequency[number]=frequency.get(number,0)+1
 
         
        for number in frequency:
            
            buckets[frequency[number]].append(number)
        
        for i in reversed(range(len(buckets))):
            for num in buckets[i]:

                most_frequant_Number_in_order.append(num)

                if len(most_frequant_Number_in_order) == k:
                    return most_frequant_Number_in_order





