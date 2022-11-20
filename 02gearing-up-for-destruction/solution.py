import fractions

def solution(pegs):

    #making a list of differece between pegs
    d = [pegs[i+1]-pegs[i] for i in range(len(pegs)-1)]
   
   #checking whether there are an even or odd amount of pegs
    if len(pegs)%2 == 0:
            evenpegs = True
    elif len(pegs)%2 == 1:
            evenpegs = False
    radius = 0

    #calculating r[0] for even pegs
    if evenpegs == True:
        add = True 
        for i in d:
            if add == True:
                radius = radius + i
                add = False
            elif add == False:
                radius = radius - i
                add = True
        radius = radius/1.5

    #calculating r[0] for odd pegs
    if evenpegs == False:
        add = True 
        for i in d:
            if add == True:
                radius = radius + i
                add = False
            elif add == False:
                radius = radius - i
                add = True
        radius = radius/0.5
   
    #calculating all the gear radii
    r = [radius]
    for i in range(len(d)):
        r += [d[i] - r[i]]
    #checking none of the gears are smaller than 1, if so returning -1,-1
    for i in r:
        if i < 1:
            return -1,-1
    #turning radius of first gear into a fraction and returning numerator and denominator 
    else:
        f = fractions.Fraction(radius).limit_denominator()
        return f.numerator, f.denominator
    
#Beyond this point was not submitted and was only used in order to test the code

listofpegs = [4,30,50] #this is the test list, alter this to try different combinations of pegs

output = solution(listofpegs)
print(output)

