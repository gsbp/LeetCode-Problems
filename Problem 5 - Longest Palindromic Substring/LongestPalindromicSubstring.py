class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

    def isPal(self, string):
        rString = string[::-1]
        return rString == string

    def getAllSubStrings(self, s):
        
        longestString = s[0]
        for i in range(len(s) - 1):
            
            center = s[i]
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                rightChar = s[right]
                leftChar = s[left]
                if(rightChar != leftChar):
                    break
                center = rightChar + center + leftChar
                left -= 1
                right += 1
            
            if len(center) > len(longestString):
                longestString = center

            if(s[i] == s[i + 1]):
                center2 = s[i] + s[i + 1]
                
                left = i - 1
                right = i + 1 + 1
                while left >= 0 and right < len(s):
                    rightChar = s[right]
                    leftChar = s[left]
                    if(rightChar != leftChar):
                        break
                    center2 = rightChar + center2 + leftChar
                    left -= 1
                    right += 1
                if len(center2) > len(longestString):
                    longestString = center2
        return longestString
    


    def lengthOfLongestSubstring(self, s: str) -> int:    
        currentString = ""
        palindromes = []
        lastI = None
        i=0       
        while i < len(s):
            currentString += s[i]
            j = i+1
            while j < len(s):                
                currentString += s[j]
                if self.isPal(currentString):                    
                    palindromes.append(currentString)
                    i = len(currentString) -1
                    currentString = ""
                j+=1
            i+=1
        
        if not palindromes:
            return s[0]
        return max(palindromes, key=len)

s = Solution()
print(s.getAllSubStrings("aaaa"))
print(s.lengthOfLongestSubstring("racecar"))