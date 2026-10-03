class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequant_Number_in_order=[]
        frequency={}

        if len(nums) == 0 :
            return most_frequant_Number_in_order

        for number in nums:
            frequency[number]=frequency.get(number,0)+1

        most_frequant_Number_in_order = sorted(frequency, key=frequency.get, reverse=True)


        answer=[]

        for i in range(k):
            answer.append(most_frequant_Number_in_order[i])

        return answer






        