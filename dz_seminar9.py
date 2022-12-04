class TikTakToeBoard:

    def __init__(self):
        self.game_list = [
        ['-','-','-'],
        ['-','-','-'],
        ['-','-','-']
        ]
        self.count = 0


#Для создания новой игры  
    def new_game(self):
        return 'Начинаем новую игру!'

#Для получения поля (список списков)
    def get_field(self):
        if self.game_list[0][0] == '-' and self.game_list[0][1] == '-' and self.game_list[0][2] == '-'\
            and self.game_list[1][0] == '-' and self.game_list[1][1] == '-' and self.game_list[1][2] == '-'\
            and self.game_list[2][0] == '-' and self.game_list[2][1] == '-' and self.game_list[2][2] == '-':
            print(self.new_game())
            return self.game_list
        else:
            return self.game_list
      

#Для проверки, есть ли победитель. Возвращает х если победил первый игрок. Возвращает 0 если победил второй игрок.
#Возвращает D если ничья. Возвращает None если можно продолжить игру.
    def ceck_field(self):
        if self.game_list[0][0] == 'X' and self.game_list[0][1] == 'X' and self.game_list[0][2] == 'X'\
            or self.game_list[0][0] == 'X' and self.game_list[1][1] == 'X' and self.game_list[2][2] == 'X'\
            or self.game_list[0][0] == 'X' and self.game_list[1][0] == 'X' and self.game_list[2][0] == 'X'\
            or self.game_list[1][0] == 'X' and self.game_list[1][1] == 'X' and self.game_list[1][2] == 'X'\
            or self.game_list[2][0] == 'X' and self.game_list[2][1] == 'X' and self.game_list[2][2] == 'X'\
            or self.game_list[0][1] == 'X' and self.game_list[1][1] == 'X' and self.game_list[2][1] == 'X'\
            or self.game_list[0][2] == 'X' and self.game_list[1][2] == 'X' and self.game_list[2][2] == 'X'\
            or self.game_list[2][0] == 'X' and self.game_list[1][1] == 'X' and self.game_list[0][2] == 'X':
            return 'Победил игрок Х. Игра завершина' 
        elif self.game_list[0][0] == '0' and self.game_list[0][1] == '0' and self.game_list[0][2] == '0'\
            or self.game_list[0][0] == '0' and self.game_list[1][1] == '0' and self.game_list[2][2] == '0'\
            or self.game_list[0][0] == '0' and self.game_list[1][0] == '0' and self.game_list[2][0] == '0'\
            or self.game_list[1][0] == '0' and self.game_list[1][1] == '0' and self.game_list[1][2] == '0'\
            or self.game_list[2][0] == '0' and self.game_list[2][1] == '0' and self.game_list[2][2] == '0'\
            or self.game_list[0][1] == '0' and self.game_list[1][1] == '0' and self.game_list[2][1] == '0'\
            or self.game_list[0][2] == '0' and self.game_list[1][2] == '0' and self.game_list[2][2] == '0'\
            or self.game_list[2][0] == '0' and self.game_list[1][1] == '0' and self.game_list[0][2] == '0':
            return 'Победил игрок 0. Игра завершина'
        elif self.game_list[0][0] != '-' and self.game_list[0][1] != '-' and self.game_list[0][2] != '-'\
            and self.game_list[1][0] != '-' and self.game_list[1][1] != '-' and self.game_list[1][2] != '-'\
            and self.game_list[2][0] != '-' and self.game_list[2][1] != '-' and self.game_list[2][2] != '-':
            return 'Ничья D. Игра завершина'
        else: 
            return 'Продолжаем играть'
        

#Устанавливает значение текущего кода в ячейку поля с координатами row, col, если это возможно, 
# переключает ход игрока, а также возвращает сообщение "Победил игрок х(0)", "Ничья", "Продолжаем играть", 
# "Клетка row, col занята", "Игра завершена"
    def mace_move(self):
        self.count += 1
        if self.count %2 != 0:
            print('Ход игрока X:')
            row = int(input('Введите первую координату (0, 1, 2): '))
            col = int(input('Введите вторую координату (0, 1, 2): '))
            if self.game_list[row][col] != '-':
                print('Клетка уже занята. Поставьте символ в другую клетку')
                row = int(input('Введите заново первую координату (0, 1, 2): '))
                col = int(input('Введите заново вторую координату (0, 1, 2): '))
                self.game_list[row][col] = 'X'
            else:
                self.game_list[row][col] = 'X'
            print(self.ceck_field())
        else:
            print('Ход игрока 0:')
            row = int(input('Введите первую координату (0, 1, 2): '))
            col = int(input('Введите вторую координату (0, 1, 2): '))
            if self.game_list[row][col] != '-':
                print('Клетка уже занята')
                row = int(input('Введите заново первую координату (0, 1, 2): '))
                col = int(input('Введите заново вторую координату (0, 1, 2): '))
                self.game_list[row][col] = '0'
            else:
                self.game_list[row][col] = '0'
            print(self.ceck_field()) 


board = TikTakToeBoard()
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')
print(board.mace_move())
print(*board.get_field(), sep = '\n')