class Solution:

    def encode(self, strs: List[str]) -> str:
     returnString=""
     for word in strs:
        returnString+=str(len(word))+"#"+word
     
     return returnString

    def decode(self, s: str) -> List[str]:
        returnString=[]
        if s=="":
            return returnString
        index=0
        while index<len(s):
            hashtagIndex=index
            while s[hashtagIndex]!="#":
                hashtagIndex+=1

            wordLength=int(s[index:hashtagIndex])
            returnString.append(s[hashtagIndex+1:hashtagIndex+wordLength+1])
            index=hashtagIndex+wordLength+1
        return returnString



