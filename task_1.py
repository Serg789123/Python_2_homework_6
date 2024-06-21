# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
from modul_date_task_1 import *

if __name__ == '__main__':
    day, month, year = map(int, argv[1:4])
    print(date_is_true(day, month, year))
