class Solution:

    def encode(self, strs: List[str]) -> str:
        
        returnString=""
        for word in strs:
            wordLength=len(word)    
            returnString+=str(wordLength)+"#"+word
        return returnString


    def decode(self, s: str) -> List[str]:
        returnList=[]
        
        index=0
        while index<len(s):
            
            hashTagIndex=index+1
            while s[hashTagIndex] !="#":
                hashTagIndex+=1
            
            wordLength=s[index:hashTagIndex]
            returnList.append(s[hashTagIndex+1:hashTagIndex+int(wordLength)+1])
            index=hashTagIndex+int(wordLength)+1
            
        return returnList

            

            

            

