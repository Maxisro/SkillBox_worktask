# import random
#
# # original_prices = [random.randint(-20, 30) for _ in range(5)]
# original_prices = [-12, 3, 5, -2, 1]
# new_prices = original_prices[:]
#
# for i in range(len(original_prices)):
#
#     if new_prices[i] < 0:
#
#         new_prices[i] = 0
#
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))

# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# print(nums[:5])
# print(nums[:-2])
# print(nums[::2])
# print(nums[1::2])
# print(nums[::-1])
# print(nums[-1::-2])

nums = [x for x in range(20)]
A = 5
B = 9
print(nums)
nums = nums[:A] + nums[B:]
print(nums)