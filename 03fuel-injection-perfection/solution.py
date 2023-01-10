def solution(n):
    nint = int(n)
    movecount = 0 #counter for how many actions have been made

    while nint != 1:
        if nint%2 == 0:        #dividing by a half is always the greatest preference (if possible)
            nint=nint/2
            movecount += 1

        elif ((nint+1)%4)==0 and nint!=3:
            nint+=1
            movecount+=1
           
        else:
            nint-=1
            movecount+=1
           
    return movecount

