class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        biggestValueRightIndex=0



        for leftIndex in range(len(prices)-1):
            
            if biggestValueRightIndex<=leftIndex:
                #print(prices[biggestValueRightIndex]," ",prices[leftIndex])
                rightIndex=leftIndex+1
                biggestValueRightIndex=rightIndex
                while rightIndex<len(prices):
                    #print(prices[biggestValueRightIndex])
                    if prices[biggestValueRightIndex]<prices[rightIndex]:
                        biggestValueRightIndex=rightIndex
                    rightIndex+=1
                    
            #print(prices[rightIndex]-prices[leftIndex])
            if profit<(prices[biggestValueRightIndex]-prices[leftIndex]):
             profit =prices[biggestValueRightIndex]-prices[leftIndex]
            
        return profit 

