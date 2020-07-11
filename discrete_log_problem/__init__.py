from .baby_giant_step import babygiantstep

def naivedlog(g,h,m):
    is_solution = False
    solution_x = None
    for x in range(1, m-1):
        is_solution = pow(g,x,m) == h
        if is_solution: return x