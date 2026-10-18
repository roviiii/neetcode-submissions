class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      hashMap={}


      for letter in s:
       hashMap[letter]=hashMap.get(letter,0)+1

      for letter in t:
         hashMap[letter]=hashMap.get(letter,0)-1

      for value in hashMap:
        if hashMap[value]!=0:
          return False

      return True 

        