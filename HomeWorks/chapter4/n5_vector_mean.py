# computing mean of a vector
from n3_vector_sum import vector_sum
def vector_mean(vectors):
    n = len(vectors)
    return vector_sum(vectors) / n

