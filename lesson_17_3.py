# A = int(input('A: '))
# B = int(input('B: '))
#
# even_list = [x for x in range(A, B+1) if x % 2 == 0]
# print(even_list)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [(x if x > 0 else 0)  for x in original_prices]
print(new_prices)