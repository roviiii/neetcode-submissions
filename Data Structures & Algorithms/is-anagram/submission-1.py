class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map={}
        if len(s) != len(t):
          return False
        
        for letter in s:
          map[letter]= map.get(letter,0)+1
          
        for letter in t:
          map[letter]=map.get(letter,0)-1
        
        for key in map:
          if map[key]!= 0:
            return False 

        return True 