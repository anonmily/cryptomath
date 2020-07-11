import math
def number_to_base(n, base):
    # Use division method to convert to an arbitrary base
    q = n
    base_representation = []
    while q != 0:
        r = q % base
        q = math.floor(q / base)
        base_representation.append(int(r))
    return base_representation

