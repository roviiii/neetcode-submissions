class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
       leftIndex=0
       longestValidWindow=0
       hashMap={}
       maxFrequency=0

       for rightIndex in range(len(s)):
        hashMap[s[rightIndex]]=hashMap.get(s[rightIndex],0)+1
        maxFrequency = max(maxFrequency,hashMap[s[rightIndex]])
        windowLength = rightIndex - leftIndex + 1
        
        #(windowLength-maxFrequency) is the ammount of changes needed to make the window valid 
        #and here we are looping until it is valid
        #and pulling left index making the window smaller 
        while (windowLength-maxFrequency)>k:
            hashMap[s[leftIndex]]-=1
            leftIndex+=1
            windowLength = rightIndex - leftIndex + 1
           
        longestValidWindow = max(longestValidWindow,windowLength)
        
        
       return longestValidWindow

        

        















"AAAAAABCDWERWABB"



