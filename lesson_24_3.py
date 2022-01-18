# class User:
#     user_name = 'Admin'
#     password = 'qwerty'
#     is_banned = False
#     friends = []
#
#     def print_info(self):
#         print('Name: {}\nPassword: {}\nBan status: {}'.format(
#             self.user_name, self.password, self.is_banned
#         ))
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
#
# user_1 = User()
# user_2 = User()
# user_2.user_name = 'Alina'
# user_1.print_info()
# user_1.add_friend('Bob')
# user_1.add_friend(user_2)
# print(user_1.friends)


class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def info(self):
        print(
            'Family name: {}\n'
            'Family funds: {}\n'
            'Having a house: {}\n'.format(
                self.surname, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value: {}'.format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased by {} USD! Current money: {}\n'.format(house_price, self.money))
        else:
            print('Not enough money!\n')


my_family = Family()
my_family.info()
print('Try to buy a house')
my_family.buy_house(10 ** 6)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy house again')
    my_family.buy_house(10 ** 6, 10)

my_family.info()
