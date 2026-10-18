class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet={}
        returnList=[]

        for word in strs:
            signiture=[0]*26
            for letter in word:
                index=ord("a")-ord(letter)
                signiture[index]+=1
            
            hashSet[tuple(signiture)]=hashSet.get(tuple(signiture),[])
            hashSet[tuple(signiture)].append(word)

        for signiture in hashSet:

            returnList.append(hashSet[signiture])


        return returnList
                