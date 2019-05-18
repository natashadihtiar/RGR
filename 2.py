import matplotlib.pyplot as plt
import matplotlib as mpl

def mnkGP(x,y): # функция которую можно использзовать в програме
              n=len(x) # количество элементов в списках
              s=sum(y) # сумма значений y
              s1=sum([1/x[i] for i in  range(0,n)]) #  сумма 1/x
              s2=sum([(1/x[i])**2 for i in  range(0,n)]) #  сумма (1/x)**2
              s3=sum([y[i]/x[i]  for i in range(0,n)])  # сумма y/x
              a= round((s*s2-s1*s3)/(n*s2-s1**2),3) # коэфициент а с тремя дробными цифрами
              b=round((n*s3-s1*s)/(n*s2-s1**2),3)# коэфициент b с тремя дробными цифрами
              s4=[a+b/x[i] for i in range(0,n)] # список значений гиперболической функции
              so=round(sum([abs(y[i] -s4[i]) for i in range(0,n)])/(n*sum(y))*100,3)   # средняя ошибка аппроксимации
              plt.title('Метод наименьших квадратов \n Аппроксимация гиперболой Y='+str(a)+'+'+str(b)+'/x\n Погрешность-'+str(so)+'%',size=10)
              plt.xlabel('Координата X', size=10)
              plt.ylabel('Координата Y', size=10)
              plt.plot(x, y, color='blue', marker='o', label='Значения координат(x,y)')
              plt.plot(x, s4, color='black', label='Функция f(x)=a+b/x')
              plt.legend(loc='best')
              plt.grid(True)
              plt.show()
x=[10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86]
y=[0.1, 0.0714, 0.0556, 0.0455, 0.0385, 0.0333, 0.0294, 0.0263, 0.0238, 0.0217,
   0.02, 0.0185, 0.0172, 0.0161, 0.0152, 0.0143, 0.0135, 0.0128, 0.0122, 0.0116] # данные для проверки по функции y=1/x
mnkGP(x,y)