print('Правила: Игрок_1 ходит крестиками, Игрок_2 - ноликами. '
      'Игроки по очереди вводят две координаты через Enter (от 0 до 2).')
print('Новая игра:')
Field = ['  0 1 2',
        '0 - - -',
        '1 - - -',
        '2 - - -']
print(*Field, sep='\n')

winner_index = ({'00', '01', '02'},
                {'10', '11', '12'},
                {'20', '21', '22'},
                {'00', '10', '20'},
                {'01', '11', '21'},
                {'02', '12', '22'},
                {'00', '11', '22'},
                {'02', '11', '20'})
# winner_index - выигрышные комбинации ij (i-номера строк; j-номера столбцов).

data_index_1 = set()      # Записываются координаты ходов Игрока_1.
data_index_2 = set()      # Записываются координаты ходов Игрока_2.
k = 0                     # Счетчик игр (для оглашения ничьи после 9й игры)

# Алгоритм вывода ходов на поле, где: x,y-координаты; xo-символ хода Игрока (x или o).
def tic_tac_toe(x, y, xo):
    Field[y + 1] = Field[y + 1][:x*2+2] + xo + Field[y + 1][x*2+3:]
    return print(*Field, sep='\n')

# Алгоритм ввода и проверки ходов Игроков:
def play():
    global x, y
    if k % 2:
        print('Игрок_2 делает ход: столбец № ', end='')
    else:
        print('Игрок_1 делает ход: столбец № ', end='')
    x = int(input())
    while x not in (0, 1, 2):
        print('Вы ввели неправильную координату, повторите ввод: ', end='')
        x = int(input())
    print('                     строка № ', end='')
    y = int(input())
    while y not in (0, 1, 2):
        print('Вы ввели неправильную координату, повторите ввод: ', end='')
        y = int(input())
    index = str(x) + str(y)
    if index in data_index_1 or index in data_index_2:
        print('Этот ход уже был! введите координаты заново.')
        play()
    elif k % 2:
        data_index_2.add(index)
    else:
        data_index_1.add(index)

# Выполнение хода Игроками:
def game():
    global k
    play()
    tic_tac_toe(x, y, 'o' if k % 2 else 'x')
    k += 1
    yield game()

# Пока не соберется выигрышная комбинация:
winner = False
while not winner:
    if k == 9:
        print('Игра окончена - ничья')
        winner = True
        break
    next(game())
    for i in range(len(winner_index)):
        if winner_index[i].issubset(data_index_1):
            print('Поздравляем Игрок_1 - Вы ВЫИГРАЛИ!')
            winner = True
        if winner_index[i].issubset(data_index_2):
            print('Поздравляем Игрок_2 - Вы ВЫИГРАЛИ!')
            winner = True
