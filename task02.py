"""
2. Преобразовать массив таким образом, чтобы сначала располагались все элементы, модуль которых не превышает 1, а
    потом - все остальные.
"""

if __name__ == "__main__":
    some_float_list = [1, 2, 0.5, 0.1, -2, -1, -0.1, -0.5]
    print('Original array:')
    print('\t', some_float_list)
    print('Sorted array:')
    print('\t', sorted(some_float_list, key=lambda x: (abs(x) >= 1, x)))

#
# Original array:
# 	 [1, 2, 0.5, 0.1, -2, -1, -0.1, -0.5]
# Sorted array:
# 	 [-0.5, -0.1, 0.1, 0.5, -2, -1, 1, 2]
#
# Process finished with exit code 0
#

