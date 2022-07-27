
class Solution:
    def reverse(self, x: int) -> int:
        s = s.strip()
        neg = False
        index = 0
        
        if len(s) <= 0:
            return 0
        
        if not s[0].isdigit():
            if s[0] == "-":
                neg = True
                index += 1
            elif s[0] == "+":
                index += 1
            else:
                return 0
        
        s = s.lstrip("0")
        rs = ""
        
        while index < len(s) :
            cChar = s[index]
            if cChar.isdigit():
                rs += cChar
            else:
                break
            index += 1
            
        if(rs == ""):
            return 0
        n = int(rs)
        
        if neg:
            n *= -1
        print(n)
        if(n <= -2 ** 31):
            n = -2 ** 31
        if(n >= (2 ** 31) - 1):
            n = (2 ** 31) - 1
        
        return n





s = Solution()
x = 10
print(s.reverse(x))
