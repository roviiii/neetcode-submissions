class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       seen=set()
       leftIndex=0
       longest=0

       for rightIndex in range(len(s)):
        while s[rightIndex] in seen :
            seen.remove(s[leftIndex])
            leftIndex+=1
        seen.add(s[rightIndex])   
        if longest<(rightIndex-leftIndex+1):

            longest=(rightIndex-leftIndex)+1

       return longest
