"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""

__all__ = ['is_queen_beat', ['double']]

import random

def is_queen_beat(position: list[list[int]]) -> bool:
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True  # ферзи не бьют др др
    else:
        return False  # ферзи бьют др др

if __name__ == '__main__':
    print(is_queen_beat([[5, 5], [3, 5], [8, 3], [2, 7], [4, 8], [6, 4], [1, 1], [7, 6]]))


def double():
    position = []
    n = 8

    for i in range(n):
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        position.append([x, y])
    print(position)
    print(set(map(tuple, position)))
    if len(position) == len(set(map(tuple, position))):
        return True
    else:
        return False

if __name__ == '__main__':
    print(double())
