# implementing dot multiplying between to vectors
def dot(v,w):
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

