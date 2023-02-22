class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        listOfChars = list(s)
        count = 0
        history = []
        checkCount = 0
        # gives list of chars
        for i in range (len(s)):
            # if its opening => we add count and 
            if listOfChars[i]=="(" :
                history.append(")")
                count += 1 
            elif listOfChars[i]=="{":
                history.append("}")
                count +=1
            elif listOfChars[i]=="[":
                history.append("]")
                count +=1
            elif listOfChars[i]==")" or listOfChars[i]=="}" or listOfChars[i]=="]":
                if count == 0:
                    result = False
                    break
                if listOfChars[i] != history[checkCount]:
                    result = False
                    checkCount += 1
                    break
                else:
                    checkCount +=1
        return result
