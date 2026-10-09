class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashResult= {}
        listResult=[]
        for word in strs:
            listKey = [0] * 26

            for letter in word:
                listKey[ord(letter) - ord("a")] += 1

            tupleKey = tuple(listKey)

            if tupleKey not in hashResult:
                hashResult[tupleKey]= []
            hashResult[tupleKey].append(word)

        for key in hashResult:
            listResult.append(hashResult[key])

        return listResult
            
