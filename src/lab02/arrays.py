def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:    
    if not nums:    
        raise ValueError("Список пуст")    
    return (min(nums),max(nums))    
    
def unique_sorted(nums: list[float | int]) -> list[float | int]:     
    return sorted(set(nums)) if nums else []       

def flatten(mat: list[list | tuple]) -> list:   
    if not mat: 
        raise ValueError("Список пуст")   

    result = []
    for row in mat:
        if not isinstance(row,(list,tuple)): 
            raise TypeError("строка не строка строк матрицы")  
        result.extend(row)  
    return result 
    


def show_min_max(x):
    try:
        print(x, "→", min_max(x))
    except ValueError:
        print(x, "→ ValueError")

def show_unique_sorted(x):
    print(x, "→", unique_sorted(x))

def show_flatten(x):
    try:
        print(x, "→", flatten(x))
    except TypeError:
        print(x, "→ TypeError")

show_min_max([3, -1, 5, 5, 0])
show_min_max([42])
show_min_max([-5, -2, -9])
show_min_max([])
show_min_max([1.5, 2, 2.0, -3.1])

print()

show_unique_sorted([3, 1, 2, 1, 3])
show_unique_sorted([])
show_unique_sorted([-1, -1, 0, 2, 2])
show_unique_sorted([1.0, 1, 2.5, 2.5, 0])

print()

show_flatten([[1, 2], [3, 4]])
show_flatten([[1], [2, 3], (4, 5)])
show_flatten([[1], [2, 3], [1]])
show_flatten([[1, 2], "ab"])