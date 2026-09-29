class Solution:

    '''
    encode:
    1. count the number of characters in each word, prepend count to string, followed by '#', followed by word
    2. add word to result

    '''

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            lenS = str(len(s))
            output += lenS
            output += "#"
            output += s
        return output


    '''
    decode:
    1. count number of chars
        1.1 take substring from start to #
        1.2 convert that string of integers -> lenS
        1.3 append substring from (index of # + 1 to lenS) to the output list
    2. return list


    5#Hello5#World

    strNum = "5"
    i = 1
    output = 
    '''  
    def decode(self, s: str) -> List[str]:

        output = []
        
        while s:

            strNum = ""
            i = 0
            while s[i] is not "#":
                strNum += s[i]
                i += 1
            num = int(strNum)

            word = s[i+1 : i+1+num]
            output.append(word)
            s = s[i+1+num:]
        
        return output





