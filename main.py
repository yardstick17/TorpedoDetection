def FileRead(file_name):
    with open(file_name, 'rb') as File:
        X = File.readlines()
    D = {}
    Matrix = []
    for i, line in enumerate(X):
        row = []
        s = ''.join(line)
        if len(s.strip()) != 0:
            for j, l in enumerate(line):
                if l in [' ', '\n']:
                    row.append(0)
                else:
                    row.append(1)
            Matrix.append(row)

    return Matrix


def CalculateBit(N):
    count = 0
    while N > 0:
        rem = N % 2
        N = N / 2
        if rem == 1:
            count += 1
    return count


def PreColoumn(Matrix, m):
    sliding_col = []
    for row in Matrix:
        pol_val = 0
        for value in row[:m]:
            pol_val = 2 * pol_val + value
        sliding_col.append(pol_val)
    pre_matrix = []
    for element in sliding_col:
        pre_matrix.append([element])

    return pre_matrix


def PreProcessing(Matrix, m):
    pre_matrix = PreColoumn(Matrix, m)
    for det_row, marix_row in zip(Matrix, pre_matrix):
        last_val = marix_row[-1]
        sub_index = 0
        for element in det_row[m:]:
            marix_row.append((last_val - det_row[sub_index] * 2**(m - 1)) * 2 +
                             element)
            last_val = (last_val - det_row[sub_index] * 2**
                        (m - 1)) * 2 + element
            sub_index += 1
    return pre_matrix


def Matching(source, target, m, h, w, target_name , cut_off):
    col_len = len(source[0])
    row_len = len(source)
    D = {}
    for i in range(row_len - m + 1):
        for j in range(col_len):
            tot, to_match = 1e-8, 1e-8
            for k in range(m):
                tot += CalculateBit(target[k][0])
                to_match += CalculateBit(target[k][0] & source[i + k][j])
            match_confidence = (to_match / tot) * 100
            if match_confidence >= cut_off:
                D[((i, j), (i + h, j + w))] = match_confidence
    for key in D:
        print 'Target Name : ', target_name, ' , Co-ordinates : ', key, ' , Degree of Confidence : ', D[
            key]
    return D
