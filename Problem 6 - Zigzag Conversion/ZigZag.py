import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pass

def test(s, numRows):
    numCols = int((len(s)/(numRows + numRows-2)) * (numRows - 1))
    if numRows == 1 or len(s) == 1:
        return s
    
    arr = [["" for i in range(numCols)] for j in range(numRows)]
    count = 0
    i = 0
    rowNumber = 2
    for i in range(numCols):
        if((i % (numRows - 1)) == 0 or i == 0):
            rowNumber = 2
            for j in range(numRows): 
                arr[j][i] = s[count]
                print(j, i, s[count])
                count += 1
                if count > len(s):
                   break
        else:
            arr[numRows - rowNumber][i] = s[count]
            count += 1
            rowNumber += 1
        if count > len(s):
                break
    
    returnString = ""
    for j in range(numRows):
        for i in range(numCols):
            returnString += arr[j][i]
    
    return returnString

def attempt(s, rows):
    if numRows == 1 or len(s) == 1:
        return s
    
    numCols = int(len(s)/(numRows)) * (numRows) + 1
    print(numCols)

    arr = [["" for i in range(numCols)] for j in range(numRows)]

    count = 0
    j = 0
    i = 0
    while count<len(s):
        if i == numRows:
            i -= 1
            while i > 0 and count<len(s):
                i -= 1
                j += 1
                arr[i][j] = s[count]
                count += 1
            i += 1

        else:
            arr[i][j] = s[count]
            count += 1
            i += 1
            
    final = ""
    for i in range(numRows):
        for j in range(numCols):
            final += arr[i][j]
            
    return final
attempt("PAHNAPLSIIGYIR", 3)

print(test("ABC", 2))



def convert(self, s: str, numRows: int) -> str:
        
        def roundup(num):
            if num > int(num):
                num = int(num) + 1
            else:
                num = int(num)
                
            return num
        
        
        mainArray =[]
        cycle = True
        for i in range(len(s)):
            cha=s[i]
            thisColumn = []
            if cycle:
                for j in range(i+numRows):
                    if (i+numRows) <= len(s):
                        thisColumn.append(cha)
                    else:
                        break
                cycle = False
            else:
                thisColumn = []
                for j in range(i+numRows-2):
                    if (i+numRows) <= len(s):                                                
                        if i%j == 0:
                            thisColumn.appen(cha)
                        else:
                            thisColumn.append(" ")
                        cycle = True
                    else:
                        break
            
                mainArray.append(thisColumn)
                
        print(mainArray)

#attempt("PAHNAPLSIIGYIR", 5)
