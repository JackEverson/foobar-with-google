def solution(n):
    nint = int(n)
    print("starting value is:" + str(n))
    movecount = 0 #counter for how many actions have been made

    while n != 1:
        if n%2 == 0:        #dividing by a half is always the greatest preference (if possible)
            n=n/2
            movecount += 1
            print("n: "+str(n)+"     movecount: "+str(movecount))

        elif ((n-1)/2)%2 != 0:
            n+=1
            movecount+=1
            print("n: "+str(n)+"     movecount: "+str(movecount))
        
        else:
            n-=1
            movecount+=1
            print("n: "+str(n)+"     movecount: "+str(movecount))

    return movecount


#testing area
solution(15)

solution(4)
