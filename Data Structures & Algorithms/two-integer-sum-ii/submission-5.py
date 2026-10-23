class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex=0
        rightIndex= len(numbers)-1


        while leftIndex<rightIndex:
            difference= target -numbers[leftIndex]
            while numbers[rightIndex]>difference:
                rightIndex-=1

            if numbers[rightIndex]==difference:
                return [leftIndex+1,rightIndex+1]

            leftIndex+=1