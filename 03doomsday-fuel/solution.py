def solution(m):
    import numpy as np
    import fractions
    import math
    
    initial_matrix = np.array(m, dtype='int')
    a_size = initial_matrix[0].size
    ordered_array = np.zeros([a_size,a_size], dtype='int')
    
    start_position = 0
    end_position = a_size - 1
    index_array = np.zeros([2, a_size], dtype='int')
    
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
            index_array[0][end_position] = i
            end_position -= 1
    
    B = np.zeros([(a_size - start_position) , a_size])
    
    idx = 0
    
    for i, x in enumerate(index_array[0]):
        if index_array[1][i] == 1:
            continue
        sum = np.sum(m[x])
        for j, y in enumerate(index_array[0]):          
            B[idx][j] = m[x][y] / sum
        idx += 1
    
    R = np.array(B[0: (a_size - start_position), 0:start_position])
    Q = np.array(B[(a_size - start_position):a_size, start_position:a_size])
    
    Q = np.array(B[0: (a_size - start_position), start_position:a_size])
    
    I = np.identity(Q[0].size)
    IminusQ = np.subtract(I,Q)
    F = np.linalg.inv(IminusQ)

    FR = np.matmul(F, R)
    
    ##### need to fix from here onwards. Issues with fractions!!!!
    
    fraction_list = list()
    for i in FR[0]:
        print(i)
        print(fractions.Fraction(i))
        fraction_list.append(fractions.Fraction(i).limit_denominator)
    
    print(fraction_list)
    
    lcm = np.lcm.reduce([fr.denominator for fr in FR[0]])
    
    output_list = [int(fr.numerator * lcm / fr.denominator) for fr in FR[0]]
    output_list.append(lcm)
    
    return lcm
                            

    


# beyond this point is for testing and debugging

# print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

# answer should be [0, 3, 2, 9, 14]
