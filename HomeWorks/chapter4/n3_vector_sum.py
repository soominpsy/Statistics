# Sum over all elements in the input vector
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = result + vector
    return result
