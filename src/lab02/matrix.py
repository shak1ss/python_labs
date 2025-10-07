def transpose(mat: list[list[int | float]]) -> list[list[int | float]]:
    if not mat:
        return []
    
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            raise ValueError("Матрица рваная")

    result = []
    for i in range(len(mat[0])):
        new_list = []
        for k in range(len(mat)):
            new_list.append(mat[k][i])  
        result.append(new_list)         
    return result 



def row_sums(mat: list[list[int | float]]) -> list[float]:
    if not mat:
        return []
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            raise ValueError("Матрица рваная")
    result = []
    for row in mat:
        s = 0.0
        for x in row:
            s += x
        result.append(s)
    return result


def col_sums(mat: list[list[int | float]]) -> list[float]:
    if not mat:
        return []
    for i in range(len(mat) - 1):
        if len(mat[i]) != len(mat[i + 1]):
            raise ValueError("Матрица рваная")
    rows = len(mat)        
    cols = len(mat[0]) 
    result = [0.0] * cols
    for j in range(cols):
        s = 0.0
        for i in range(rows):
            s += mat[i][j]
        result[j] = s
    return result



def show_transpose(m):
    try:
        print(f"{str(m):<25} → {transpose(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

def show_row_sums(m):
    try:
        print(f"{str(m):<25} → {row_sums(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

def show_col_sums(m):
    try:
        print(f"{str(m):<25} → {col_sums(m)}")
    except ValueError:
        print(f"{str(m):<25} → ValueError")

show_col_sums([[1, 2, 3], [4, 5, 6]])   
show_col_sums([[-1, 1], [10, -10]])    
show_col_sums([[0, 0], [0, 0]]) 
show_col_sums([[1, 2], [3]])    