#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.
#*Пример:
#385916 -> yes
#123456 -> no

numTick = (input('Введите шестизначный номер билета:'))
if len(numTick) == 6:
    num1 = int (numTick[0])
    num2 = int (numTick[1])
    num3 = int (numTick[2])
    num4 = int (numTick[3])
    num5 = int (numTick[4])
    num6 = int (numTick[5])
    if (num1 + num2 + num3) == (num4 + num5 + num6):
        print('Поздравляю! Ваш билет счастливый!')
    else:
        print('В этот раз вам не повезло(')
else:
    print('Вероятно, вы ошиблись!')
    print('Попробуйте еще раз!')
