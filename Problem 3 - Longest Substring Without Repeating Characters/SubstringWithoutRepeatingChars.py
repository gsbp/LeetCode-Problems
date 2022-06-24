class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:    
        longString = [""]
        longIndex = 0
        lastI = None
        i=0        
        while i < len(s):
            if (i>1):
                print("this")
                lastI = s[(i-1)]                   
            if s[i] != lastI and s[i] not in longString[longIndex] and lastI:
                longString[longIndex] += s[i]                    
                print(str(i) + " - case1")
            elif s[i] in longString[longIndex] and i > 1:
                repeat = longString[longIndex].find(s[i])
                previousString = longString[longIndex][repeat+1:]
                
                print ("Previous substring: %s" % previousString)
                longString.append(previousString)
               

                longIndex += 1
                longString[longIndex] += s[i]
                print(str(i) + " - case2")
            else:
                if s[i] not in longString[longIndex]:
                    longString[longIndex] += s[i]
                print(str(i) + " - case3")
            print (longString)
            i+=1
        return len(max(longString, key=len))


s = ["bbbbb", "dvdf", "abcabcbb"]

a = Solution()
for i in s:
    print(a.lengthOfLongestSubstring(i))