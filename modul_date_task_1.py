def _is_leap(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def date_is_true(day, month, year):
    check_days ={
        1: 31,
        2: 29 if _is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    max_day = check_days.get(month)
    if not max_day or year > 9999 or year < 1 or day > max_day or day < 1:
        return False
    else:
        return  True


if __name__ == '__main__':
    print(date_is_true(29, 2, 2024))


