# def fact(x):
#     if x == 1:
#         return 1
#     return  fact(x-1) * x
#
# print(fact(4))


# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(5))

def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom('fazaf'))