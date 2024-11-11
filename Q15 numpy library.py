#Python code to demonstrate Numpy Library
import numpy as np
#Creating 1D arrays
array_a = np.array([1,2,3])
array_b = np.array([4,5,6])
#Element-wise addition of two array
sum_array = array_a + array_b   
#Calculating the mean of the elements in array_a
mean_value = np.mean(array_a)
#Calculating the standard deviation of elements in array_a
std_dev =np.std(array_a)  #Output: 0.816496580927776
#Display results
print(f"Array Sum:{sum_array}")
print(f"Mean of Array:{mean_value}")
print(f"Standard Deviation of Array:{std_dev}")
