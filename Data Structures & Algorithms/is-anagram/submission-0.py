class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          return False 
        
        dic ={}

        for letter in s :
          dic[letter] = dic.get(letter,0)+1

        for letter in t:
          if letter not in dic:
            return False 
          
          
          dic[letter] = dic[letter]-1

        for value in dic:
           if dic[value] !=0:
            return False 

        return True 
        