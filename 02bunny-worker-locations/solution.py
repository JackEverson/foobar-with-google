def solution(x, y):
    
    position = 0
    
    for i in range(1, (x+1)):
        position = position + i
        
    for i in range(y-1):
        foobar = x + i
        position = position + foobar
    
        
    return str(position)

#note that I did not submit the code below this point, this was just for my own testing purposes
test = solution(2,2)

print(str(test))
