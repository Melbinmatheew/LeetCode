class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            print(i)
            if s[i]=='(' or s[i]== '[' or s[i]== '{':
                stack.append(s[i])
            elif (s[i]==')' or s[i]== ']' or s[i]== '}') and len(stack)==0:
                return False
            elif ( s[i]==')' and stack[-1]=='(' ) or  ( s[i]==']' and stack[-1]=='[' )or ( s[i]=='}' and stack[-1]=='{' ):
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False