def solution(x, y):
    #Attempting to work in reverse
    M = int(x)
    F = int(y)
    steps = 0
    while True:
        if M == 1 and F == 1:           #if values are 1 and 1 then we have reached our goal
            return str(steps)
        
        elif M <= 0 or F <= 0 or M == F:          #if a value has dropped below 1 then it is an impossible combination
            return "impossible"
        
        elif M > (2*F):                     #optimising if M is much larger than F
            steps=steps + ((M//F)-1)
            M = M-(((M//F)-1)*F)
            
                   
        elif M > F:                     #if M>F then subtract F from M
            M = M-F
            steps+=1
        
        elif F>(2*M):                       #if F>M then subtract M from F
            steps= steps + ((F//M)-1)
            F = F-(((F//M)-1)*M)
            
            
        elif F>M:                       #if F>M then subtract M from F
            F=F-M
            steps+=1


test = solution('2', '4')   
print(test)   
 
'''   
#Test area!!!!!!!

assert solution('4', '7') == '4'

assert solution ('2', '1') == '1'

assert solution ('2', '4') == 'impossible'

'''