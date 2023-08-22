"""
1. В одномерном массиве, содержащим n вещественных элементов, вычислить:
    1.1. номер минимального элемента массива;
    1.2. сумму элементов массива, расположенных между первым и вторым отрицательными элементами.
"""
import random as rnd
import numpy as np
from numpy import ndarray as array


def task_1_1(arr: array):
    return arr.argmin(), arr.min()


def task_1_2(arr: array):
    to_summ = 0
    res = 0
    for item in arr:
        if item < 0:
            to_summ += 1
        else:
            if to_summ == 1:
                res += item
            elif to_summ > 1:
                break
    return res


if __name__ == "__main__":
    n_count = rnd.randint(10, 20)
    base_array: array = np.zeros(shape=n_count, dtype=int)
    for _ in range(base_array.shape[0]):
        base_array[_] = rnd.randint(-100, 100)
        if _ % 5 == 0: print()
        print(f'a[{_}]={base_array[_]}'.ljust(15, ' '), end=' ')

    res_1_1 = task_1_1(base_array)

    print("\n")
    print(f'Минимальный элемент: a[{res_1_1[0]}] = {res_1_1[1]}')
    print(f'Сумма элементов массива: {task_1_2(base_array)}')

#
# a[0]=58         a[1]=66         a[2]=-88        a[3]=74         a[4]=10
# a[5]=82         a[6]=13         a[7]=-31        a[8]=-93        a[9]=-70
# a[10]=-96       a[11]=32        a[12]=24        a[13]=86        a[14]=-25
# a[15]=48        a[16]=-27       a[17]=61        a[18]=-50
#
# Минимальный элемент: a[10] = -96
# Сумма элементов массива: 179
#
# Process finished with exit code 0
#
