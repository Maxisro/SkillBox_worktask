# A = int(input('Левая граница: '))
# B = int(input('Правая граница: '))
#
# list_cube = [x ** 3 for x in range(A, B + 1)]
# list_square = [x ** 2 for x in range(A, B + 1)]
#
# print(f'Список кубов чисел в диапазоне от {A} до {B}:', list_cube)
# print(f'Список квадратов  чисел в диапазоне от {A} до {B}:', list_square)


# word = input('Введите строку: ')
# symb = input('Введите символ: ')
#
# doublet_list = [x * 2 for x in word]
# symb_list = [x + symb for x in doublet_list]
#
# print('Список удвоенных символов:', doublet_list)
# print('Склейка с дополнительным символом:', symb_list)

def price_rise(price, rise):
   return round(price * (1 + rise / 100),2)

price = [float(input('Цена на товар: ')) for x in range(5)]
first_year = float(input('Повышение на первый год: '))
second_year = float(input('Повышение на второй год: '))
first_price = [price_rise(i_price, first_year)for i_price in price]
second_price = [price_rise(i_price, second_year)for i_price in first_price]

print('Сумма цен за каждый год:',sum(price),
                                 sum(first_price),
                                 sum(second_price)
      )
