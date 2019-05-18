import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import *
from tkinter import messagebox

error = 0 #инициализация погрешности
A = 0 #инициализация коэфициента а
B = 0 #инициализация коэфициента b

def MNK(x, y):  # функция для решения с помощью метода наименьших квадратов
    n = len(x)  # общее количсевто элементов
    s = sum(y)  # сумма значений y
    s1 = sum([1 / x[i] for i in range(0, n)])  # сумма 1/x
    s2 = sum([(1 / x[i]) ** 2 for i in range(0, n)])  # сумма (1/x)^2
    s3 = sum([y[i] / x[i] for i in range(0, n)])  # сумма y/x
    a = round((s * s2 - s1 * s3) / (n * s2 - s1 ** 2), 3)  # коэфициент а
    b = round((n * s3 - s1 * s) / (n * s2 - s1 ** 2), 3)  # коэфициент b
    s4 = [a + b / x[i] for i in range(0, n)]  # список значений гиперболической функции
    global A # инициализация глобальной переменной а
    A = a
    global B # инициализация глобальной переменной b
    B = b
    so = round(sum([abs(y[i] - s4[i]) for i in range(0, n)]) / (n * sum(y)) * 100, 3)  # средняя ошибка аппроксимации
    global error # инициализация глобальной переменной error
    error = so
    plt.title('Метод наименьших квадратов!' + '\n' +'Аппроксимация: ' + str(a) + '+' + str(b) + '/x\n Погрешность:' + str(so) + '%', size=10)
    plt.xlabel('Координата x', size=10)
    plt.ylabel('Координата y', size=10)
    plt.plot(x, y, color='blue', linestyle=' ', marker='o', label='Координаты х и у')
    plt.plot(x, s4, color='black', linewidth=2, label='Значения x функции a+b/x')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()


def start(): # ввод значений пользователем
    X = [float(k) for k in inputX.get().split(",")]
    print(X)
    Y = [float(k) for k in inputY.get().split(",")]
    print(Y)
    MNK(X, Y)


root = Tk()
root.title("Метод наименших квадратов!")# создание оглавления
root.geometry("500x500")
inputX = StringVar()
inputY = StringVar()
X_label = Label(text="Координаты х:" +"\n"+ "(ввод через запятую без пробела)")# описанеи для пользователя
Y_label = Label(text="Координаты у:" +"\n"+ "(ввод через запятую без пробела)")# описанеи для пользователя

X_label.grid(row=1, column=2, sticky="w")
Y_label.grid(row=2, column=2, sticky="w")

inputX_entry = Entry(textvariable=inputX)# поля ввода для пользователя
inputX_entry.grid(row=1, column=3, padx=30, pady=30)
inputY_entry = Entry(textvariable=inputY)
inputY_entry.grid(row=2, column=3, padx=10, pady=10)

button = Button(root, text="Рассчитать", command=start)# кнопка для рассчета
button.place(relx=.4, rely=.4, anchor="c")

root.mainloop()
file = open('RGR.txt', 'w')# запись полученных результатов в файл
file.write('Полученный результат: \n' +' x: '+ inputX.get() +'; ' + '\t' + 'y: ' + inputY.get() + ';'+'\n' + 'a: ' + str(A) + '   b: ' + str(
    B) + ';'+'\n' + 'погрешность: ' + str(error))
file.close()