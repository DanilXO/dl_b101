__author__ = 'Филиппов Иван Викторович'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть


print('Первым двум условиям соответствую a = 0 и ∞, третьему только ∞')
import math
a = math.inf
print(bool(a == a**2))
print(bool(a == a*2))
print(bool(a > 999999))

