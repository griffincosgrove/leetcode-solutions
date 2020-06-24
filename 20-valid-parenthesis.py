'''
    Summary: we want to determine if there are any chars without matches. must be in the correct order.
    
    inputs:
        arg1: s:str - the string of symbols
    outputs:
        return bool
    Approach 1 : use a stack to track if any symbols were added and never received a closing pair.
    
    Edge case: empty strings are valid/true
    
    psudeo - declare stack
             declare list that contain left and right symbols
             loop through the arg string
             add left symbols to the stack
             if we parse a right symbol and the left is on there pop the left symbol off
             else return false - because we cannot have a right symbol before a left symbol
             must be in the correct order
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = {'(', '[', '{'} # set
        right = {')', ']', '}'} # set
        
        
        if not s: # take care of edge case where s is empty
            return True
        if len(s) %2 != 0: # s must be even to return true
            return False
        
        for symbol in s:
            if symbol in left:
                stack.append(symbol)
            elif symbol in right:
                if not stack:
                    return False
                elif symbol == ')' and stack[-1] == '(':
                    stack.pop(-1)
                elif symbol == ']' and stack[-1] == '[':
                    stack.pop(-1)
                elif symbol == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else: return False
        if not stack:
            return True
        else:
            return False
