class Solution:
    def defangIPaddr(self, address: str) -> str:
        returnString = ""
        for charector in address:
            if charector == '.':
                x = "[" + charector + "]"
                returnString += x
            else:
                returnString += charector                
        return returnString

