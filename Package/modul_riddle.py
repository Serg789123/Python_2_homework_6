__all__ = ['riddle']

def riddle(riddle_text: str, answer: list[str], count: int = 3) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка №{nn}: ').lower()
        if ans in answer:
            return nn
    return 0

if __name__ == '__main__':
    result = riddle('Зимой и летом одним цветом', ['ёлка', 'ель', 'сосна'])
    print(f'Загадка разгадана с {result}й попытки!' if result > 0 else 'Загадка не разгадана :(')

