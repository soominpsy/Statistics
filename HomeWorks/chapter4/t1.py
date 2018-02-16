import n1_vector_add
from n1_vector_add import vector_add
from n2_vector_subtract import vector_subtract
from n3_vector_sum import vector_sum
from n4_scalar_multiply import scalar_multiply
from n5_vector_mean import vector_mean
import n14_friends

vector1 = [1,2,3,4,5,6,7]
vector2 = [3,4,3,1,2,3,4]
vector22 = [3.0, 4.0, 3.0, 1.0, 2.0, 3.0, 4.0]
# type difference between vector2 and vector22

Add1 = vector_add(vector1, vector2)
print(Add1)

Add2 = n1_vector_add.vector_add(vector1, vector2)
print(Add2)

Subtract = vector_subtract(vector1, vector2)
print(Subtract)

Sum = vector_sum(vector1)
print(Sum)

Scalar_mul = scalar_multiply(10,vector1)
print(Scalar_mul)

Mean1 = vector_mean(vector1)
Mean2 = vector_mean(vector2)
Mean22 = vector_mean(vector22)
print(Mean1)
print(Mean2)
print(Mean22)

print(n14_friends.friendships)
