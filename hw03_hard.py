# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y


prl_count = 0
while prl_count != 4:
        u_txt = input('Введите уравнение прямой вида "y = kx + b": ')
        prl_count = u_txt.count(' ')
u_lst = u_txt.split(' ')
k = u_lst[2][:-1]
b = u_lst[4]
if u_lst[3] == '+':
        y = float(k) * x + float(b)
else:
        y = float(k) * x - float(b)
print(f'Координата у = {y}')



# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат

date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

data_in = input('Введите дату ДД.ММ.ГГГГ: ')
data_list = data_in.split('.')
dict_months = {
'01': 31,
'02': 28,
'03': 31,
'04': 30,
'05': 31,
'06': 30,
'07': 31,
'08': 31,
'09': 30,
'10': 31,
'11': 30,
'12': 31,
}
result = 'Некоректная дата'

if len(data_list[0]) == 2 and len(data_list[1]) == 2 and len(data_list[2]) == 4:
        if 1 <= int(data_list[2]) <= 9999:
                if 1 <= int(data_list[1]) <= 12:  
                        if 0< int(data_list[0]) <= dict_months[data_list[1]]:
                                result = 'Корректная дата'
print(result)





# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
    


tower = []
K = 1
for N in range(1, 20):
        tower.append(list(range(K, K + N)))
        print(list(range(K, K + N)))
        K = K + N
NUM = int(input('Введите число: '))
for M in tower:
    for R in M:
        if R == NUM:
            print(tower.index(M) + 1, M.index(R) + 1)























