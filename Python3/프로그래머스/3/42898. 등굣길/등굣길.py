def solution(m, n, puddles):
    field = [[0] * (m + 1) for _ in range(n + 1)]
    field[1][1] = 1
    
    puddles = set(map(tuple, puddles))
    puddles.add((1, 1))
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j, i) not in puddles:
                field[i][j] = (field[i - 1][j] + field[i][j - 1]) % 1000000007
    
    return field[n][m]