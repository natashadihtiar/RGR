import numpy as np
from math import sqrt

def cubic_interp1d(x0, x, y):

    #Интерпретация 1-D функцию, используя кубические сплайны с точными граничными условиями .
    # x0: float или 1d-массив
    # x: (N,) array_like -  массив реальных значений.
    # y: (N,) array_like - массив реальных значений.
    # Длина у вдоль осей интерполяции должна быть равна длине х.

    plt.title("Кубический сплайн с точными граничными условиями ")
    x = np.asfarray(x)
    y = np.asfarray(y)

    # удаление не конечных значений:
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x) #сортировка
        x = x[indexes]
        y = y[indexes]

    size = len(x) #длина по оси х

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # выделение матриц:
    Arr = np.empty(size)
    Arr_1 = np.empty(size-1)
    z = np.empty(size)


    Arr[0] = sqrt(12*xdiff[0])# заполнение диагонали матрицы
    Arr_1[0] = 0.0
    B0 = 5.0 # точные граничные условия
    z[0] = B0 / Arr[0]

    for i in range(1, size-1, 1):
        Arr_1[i] = xdiff[i-1] / Arr[i-1]
        Arr[i] = sqrt(1*(xdiff[i-1]+xdiff[i]) - Arr_1[i-1] * Arr_1[i-1])
        Bi = 4*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Arr_1[i-1]*z[i-1])/Arr[i]

    i = size - 1
    Arr_1[i-1] = xdiff[-1] / Arr[i-1]
    Arr[i] = sqrt(2*xdiff[-1] -Arr_1[i-1] * Arr_1[i-1])
    Bi = 2.0 # точные граничные условия
    z[i] = (Bi - Arr_1[i-1]*z[i-1])/Arr[i]

    # решение [Arr.T][x] = [y]
    i = size-1
    z[i] = z[i] / Arr[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Arr_1[i-1]*z[i+1])/Arr[i]

    # нахождение индексов:
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # рассчет кубического значения:
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
         zi1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    return f0

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    x = np.linspace(0, 10, 10)
    y = np.sin(x)
    plt.scatter(x, y)

    x_new = np.linspace(0, 10, 300)
    plt.plot(x_new, cubic_interp1d(x_new, x, y))

    plt.show()
