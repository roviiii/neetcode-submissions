class Solution:
    def isPalindrome(self, s: str) -> bool:
        prefix=0
        postfix=len(s)-1

        while prefix<postfix:
            while prefix<postfix and not s[prefix].isalnum():
                  prefix+=1

            while prefix<postfix and  not s[postfix].isalnum():
                 postfix-=1
            
            if s[prefix].lower()!=s[postfix].lower():
                return False
            prefix+=1
            postfix-=1


        return True