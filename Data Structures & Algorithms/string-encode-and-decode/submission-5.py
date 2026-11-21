class Solution:

    def encode(self, strs: List[str]) -> str:
        returnString=""
        for word in strs:
            returnString+=str(len(word))+"#"+word

        return returnString


    def decode(self, s: str) -> List[str]:
        returnList=[]
        index=0
        while index<len(s):
            
            hashIndex=index
            while s[hashIndex]!= "#":
                hashIndex+=1
            wordLength=int(s[index:hashIndex])

            returnList.append(s[hashIndex+1:hashIndex+wordLength+1])
            index=hashIndex+wordLength+1
        return returnList


            
                
