# a shout out to Ivanseed at https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md. This really helped me get my head around Markov absorbing chains (noting a have very little experience with linear algebra so I learnt ALOT!)
# Also a shout out to KaustubhRakhade's comment here https://gist.github.com/algomaster99/782b898177ca37bfbf955cec416bb6a4. This helped me clean up my data transformations before this I was trying to use the fractions module which kept either outputting strange data or was just outright erroring out.

def solution(m):
    import numpy as np
    active = []
    terminal = []
    
    for i, row in enumerate(m):
        (active if sum(row) else terminal).append(i)
    
    if 0 in terminal:
        x = [1] + [0]*len(terminal[1:]) + [1]
        return x
    
    active_matrix = np.matrix(m, dtype=float)[active, :]
    

    percent_chance_matrix = active_matrix / active_matrix.sum(1) # matrix of chance of changing into something rather than value of it, this only repesents the active states
    
    Q = percent_chance_matrix[:, active]
    R = percent_chance_matrix[:, terminal]   # separating Q and R matrixes using what is active and what is terminal states
    I = np.identity(len(Q))  
    F = np.linalg.inv(I - Q)
    
    cd = np.prod(active_matrix.sum(1)) #common denominator
    
    B = F[0] * R * cd / np.linalg.det(F)    #this is the point my understanding of the math starts to give out, need to learn more linear algebra
       
    final_list = B.round().astype(int).A1
    gcd = np.gcd.reduce(final_list)
    final_list = (final_list/gcd).astype(int)
    lcd = final_list.sum() 
    final_list = np.append(final_list, lcd)
    
    return final_list
    
    # print("percent chance matrix")
    # print percent_chance_matrix
    # print("Q")
    # print Q
    # print("R")
    # print R
    # print("F")
    # print F
    # print "B"
    # print B
    # print "lcd"
    # print lcd

    
test_list = [0]    
    
solution(test_list)    

solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
# answer should be [0, 3, 2, 9, 14]

solution([[0,1], [0,0]])
print(solution([[0, 1, 1, 1, 1,],  [0, 0, 0, 0, 0,], [1, 1, 0, 1, 1,], [0, 0, 0, 0, 0,], [1, 1, 1, 1, 0,] ]))
