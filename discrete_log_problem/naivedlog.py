def naivedlog(m, g,h):
    is_solution = False
    solution_x = None
    for x in range(1, m-1):
        is_solution = pow(g,x,m) == h
        if is_solution: return x
    raise Exception('No discrete log found for g=%s, h=%s, m=%s' % (g, h, m))