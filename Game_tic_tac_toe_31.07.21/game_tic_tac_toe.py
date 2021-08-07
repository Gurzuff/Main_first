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

data_index_1 = set()  # Записываются координаты ходов Игрока_1.
data_index_2 = set()  # Записываются координаты ходов Игрока_2.
k = 0  # Счетчик игр (для оглашения ничьи после 9й игры)


def tic_tac_toe(x, y, xo):
    '''Алгоритм вывода ходов на поле, где: x,y-координаты;
       xo-символ хода Игрока (x или o).'''
    Field[y + 1] = Field[y + 1][:x * 2 + 2] + xo + Field[y + 1][x * 2 + 3:]
    return print(*Field, sep='\n')


def play():
    '''Алгоритм ходов и проверки корректности ввода координат.'''
    global x, y
    if k % 2:
        print('Игрок_2 делает ход: столбец № ', end='')
    else:
        print('Игрок_1 делает ход: столбец № ', end='')
    x = int(input())
    while x not in (0, 1, 2):
        print('Вы ввели неправильную координату, повторите ввод: ', end='')
        x = input()
        if x.isdigit():
            x = int(x)
    print('                     строка № ', end='')
    y = int(input())
    while y not in (0, 1, 2):
        print('Вы ввели неправильную координату, повторите ввод: ', end='')
        y = input()
        if y.isdigit():
            y = int(y)
    index = str(x) + str(y)
    if index in data_index_1 or index in data_index_2:
        print('Этот ход уже был! введите координаты заново.')
        play()
    elif k % 2:
        data_index_2.add(index)
    else:
        data_index_1.add(index)


def game():
    '''Выполнение хода Игроками.'''
    global k
    play()
    tic_tac_toe(x, y, 'o' if k % 2 else 'x')
    k += 1
    yield game()


winner = False  # Пока не соберется выигрышная комбинация:
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
