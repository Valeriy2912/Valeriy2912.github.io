# Калькулятор ипотеки
# Некая сумма взята под определенный процент в год в банке.
# Выплаты по кредиту производятся раз в месяц
# Предложить алгоритм, позволяющий вычислить срок выплаты кредита и размер переплаты
# Разница между фактически выплаченной банку суммой и суммы, взятой в кредит
summ = int(750000)
percent = float(9.5)
percent_month = float(percent/12)
payment = int(25000)
# print("проценты", "осн. долг", "\tсумма") #Суммы выплат за каждый месяц
count = 0
# размер переплаты
a = 0
x=0
while summ > 0:
    count += 1
    percent_payment = percent_month * summ / 100
    main_debit = payment-percent_payment
    summ -= main_debit
    # if summ > 0:
    # Суммы выплат за каждый месяц
    #     print(int(percent_payment), '\t', int(main_debit), '\t\t', int(summ))
    # else:
    # сумма последнего платежа
    #     payment += summ
    # сумма последнего платежа по основному долгу
    #     main_debit = payment - percent_payment
    # Суммы выплат за каждый месяц
    #     print(int(percent_payment), '\t', int(main_debit), '\t\t', int(0))
    #     break
    a += percent_payment
if count // 12 > 0:
    print('Вы выплатите банку долг за', count // 12, 'год/года/лет', count % 12, 'месяц/месяцев')
else:
    print('Вы выплатите банку долг за', count % 12, 'месяц/месяцев')
print('Переплата составит', int(a))
input('Нажмите Enter для выхода из программы')
