# This was my first attempt at the code. While I was passing a number of the tests this code was never fully successful. I was having issues with converting between data and object types so I decided to restart from scratch. 

def solution(m):
    import numpy as np
    import fractions
    
    initial_matrix = np.array(m, dtype='int')
    a_size = initial_matrix[0].size
    
    if initial_matrix.size == 1:
        return [1,1]
    
    if np.sum(initial_matrix[0]) == 0:
        return [1] + [0]*(a_size-1) + [1]
    
    if initial_matrix.size == 4 and initial_matrix[0][1] == 1:
        return [1,1]
        
    start_position = 0
    end_position = a_size - 1
    index_array = np.zeros([2, a_size], dtype='int')
    
    terminial_states = 0
    for i in initial_matrix:
        if i.sum() == 0:
            terminial_states += 1
            
    terminial_states_ref = terminial_states
    for i, x in enumerate(initial_matrix[:]):
        absorbing = True
        for y in x[:]:
            if y != 0:
                absorbing = False
                break
        if absorbing == True:
            index_array[0][start_position] = i
            index_array[1][start_position] = 1
            start_position += 1
        else:
            index_array[0][terminial_states_ref] = i
            terminial_states_ref += 1
    
    B = np.zeros([(a_size - start_position) , a_size])
    
    idx = 0
    
    for i, x in enumerate(index_array[0]):
        if index_array[1][i] == 1:
            continue
        sum = float(0)
        for q in m[int(x)]:
            sum += q
        for j, y in enumerate(index_array[0]):          
            B[idx][j] = float(m[int(x)][int(y)] / sum)
        idx = 1
    
    R = np.array(B[0: (a_size - start_position), 0:start_position])
    Q = np.array(B[0: (a_size - start_position), start_position:a_size])
    I = np.identity(len(Q[0]))
    print "R"
    print R
    print "Q"
    print Q
    IminusQ = np.subtract(np.asmatrix(I),np.asmatrix(Q))
    print "I - Q"
    print IminusQ
    
    # F = np.linalg.inv(IminusQ)
    F = IminusQ ** (-1)
    print(F)
    print(type(F))
    FR = np.matmul(F, R)
    fraction_list = list()
    for i in FR[0]:
        fraction_list.append(fractions.Fraction(i).limit_denominator())
    
    numerator_list = list()
    denominator_list = list()
    for i in fraction_list:
        numerator_list.append(i.numerator)
        denominator_list.append(i.denominator)
    
    lcm = np.lcm.reduce(denominator_list)
    # gcd = np.gcd.reduce(fraction_list)
        
    
    
    for idx, i in enumerate(numerator_list):
        x = lcm / denominator_list[idx]
        numerator_list[idx] = (x * i)
    
    numerator_list.append(lcm)


    return numerator_list
                            

    


# beyond this point is for testing and debugging

# print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))

# # [7, 6, 8, 21]

# print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
# # answer should be [0, 3, 2, 9, 14]

# print(solution([0]))

# print(solution([[0,1], [0,0]]))

# import numpy as np
# y = np.zeros([10,10])
# print(solution(y))

print(solution([[0, 1, 1, 1, 1,],  [0, 0, 0, 0, 0,], [1, 1, 0, 1, 1,], [0, 0, 0, 0, 0,], [1, 1, 1, 1, 0,] ]))
