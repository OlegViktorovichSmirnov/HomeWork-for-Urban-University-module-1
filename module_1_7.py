# Дополнительное практическое задание по модулю: "Базовые структуры данных."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
# Предисловие:
# Сложность подобных задач заключается в:
# Отсутствии чёткого алгоритма решения. Его вы должны придумать сами на основе полученных ранее знаний (синтаксиса и инструментов).
# Объединении большинства тем изученного модуля.
# Предполагаемом большом объёме решения.
#
# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
#
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
#
#
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).

# Т.к. сумма чисел списка - число, сумма списков - список. и деление списка на число запрещено, вычисляем среднее
# поэлементно используя sum для суммирования и len для вычисления длины каждого списка

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = [5, 3, 3, 5, 4]
average_a = sum(a) / len(a)
print(f'{average_a}')
b = [2, 2, 2, 3]
average_b = sum(b) / len(b)
print(f'{average_b}')
c = [4, 5, 5, 2]
average_c = sum(c) / len(c)
print(f'{average_c}')
d = [4, 4, 3]
average_d = sum(d) / len(d)
print(f'{average_d}')
e = [5, 5, 5, 4, 5]
average_e = sum(e) / len(e)
print(f'{average_e}')

grades_changed = [average_a, average_b, average_c, average_d, average_e]
print(f'{grades_changed}')

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list(students)

# Так как множество не упорядоченно, то нам необходимо упорядочить его по алфавиту при помощи функции sorted

student_sorted = sorted(students)
print(f'Список студентов: {student_sorted}')

# Создаём словарь из списков и упорядоченного множества.

my_dict = dict(zip(student_sorted, grades_changed))
print(f'{my_dict}')

