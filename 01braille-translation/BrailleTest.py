
def solution(s):
    
    wordSol = s
    solutionCode = ""
    i = 0
    strLength = len(s)
    
    while i < strLength:
        
        
        x = wordSol[i]
        i = i+1
        if x == 'a':
            solutionCode = solutionCode + '100000'
        elif x == 'b':
            solutionCode = solutionCode + '110000'
        elif x == 'c':
            solutionCode = solutionCode + '100100'
        elif x == 'd':
            solutionCode = solutionCode + '100110'
        elif x == 'e':
            solutionCode = solutionCode + '100010'
        elif x == 'f':
            solutionCode = solutionCode + '110100'
        elif x == 'g':
            solutionCode = solutionCode + '110110'
        elif x == 'h':
            solutionCode = solutionCode + '110010'
        elif x == 'i':
            solutionCode = solutionCode + '010100'
        elif x == 'j':
            solutionCode = solutionCode + '010110'
        elif x == 'k':
            solutionCode = solutionCode + '101000'
        elif x == 'l':
            solutionCode = solutionCode + '111000'
        elif x == 'm':
            solutionCode = solutionCode + '101100'
        elif x == 'n':
            solutionCode = solutionCode + '101110'
        elif x == 'o':
            solutionCode = solutionCode + '101010'
        elif x == 'p':
            solutionCode = solutionCode + '111100'
        elif x == 'q':
            solutionCode = solutionCode + '111110'
        elif x == 'r':
            solutionCode = solutionCode + '111010'
        elif x == 's':
            solutionCode = solutionCode + '011100'
        elif x == 't':
            solutionCode = solutionCode + '011110'
        elif x == 'u':
            solutionCode = solutionCode + '101001'
        elif x == 'v':
            solutionCode = solutionCode + '111001'
        elif x == 'w':
            solutionCode = solutionCode + '010111'
        elif x == 'x':
            solutionCode = solutionCode + '101101'
        elif x == 'y':
            solutionCode = solutionCode + '101111'
        elif x == 'z':
            solutionCode = solutionCode + '101011'
            
        elif x == 'A':
            solutionCode = solutionCode + '000001100000'
        elif x == 'B':
            solutionCode = solutionCode + '000001110000'
        elif x == 'C':
            solutionCode = solutionCode + '000001100100'
        elif x == 'D':
            solutionCode = solutionCode + '000001100110'
        elif x == 'E':
            solutionCode = solutionCode + '000001100010'
        elif x == 'F':
            solutionCode = solutionCode + '000001110100'
        elif x == 'G':
            solutionCode = solutionCode + '000001110110'
        elif x == 'H':
            solutionCode = solutionCode + '000001110010'
        elif x == 'I':
            solutionCode = solutionCode + '000001010100'
        elif x == 'J':
            solutionCode = solutionCode + '000001010110'
        elif x == 'K':
            solutionCode = solutionCode + '000001101000'
        elif x == 'L':
            solutionCode = solutionCode + '000001111000'
        elif x == 'M':
            solutionCode = solutionCode + '000001101100'
        elif x == 'N':
            solutionCode = solutionCode + '000001101110'
        elif x == 'O':
            solutionCode = solutionCode + '000001101010'
        elif x == 'P':
            solutionCode = solutionCode + '000001111100'
        elif x == 'Q':
            solutionCode = solutionCode + '000001111110'
        elif x == 'R':
            solutionCode = solutionCode + '000001111010'
        elif x == 'S':
            solutionCode = solutionCode + '000001011100'
        elif x == 'T':
            solutionCode = solutionCode + '000001011110'
        elif x == 'U':
            solutionCode = solutionCode + '000001101001'
        elif x == 'V':
            solutionCode = solutionCode + '000001111001'
        elif x == 'W':
            solutionCode = solutionCode + '000001010111'
        elif x == 'X':
            solutionCode = solutionCode + '000001101101'
        elif x == 'Y':
            solutionCode = solutionCode + '000001101111'
        elif x == 'Z':
            solutionCode = solutionCode + '000001101011'
        else:
            solutionCode = solutionCode + '000000'
    
    
    return solutionCode


while True:
    wordString = input()
    codeString = solution(wordString)
    
    print(codeString)
    