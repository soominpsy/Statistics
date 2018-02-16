#Notice the length of two input vectors must be same
# adding two vecotrs elements in element-wise way
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]  


