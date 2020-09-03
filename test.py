# def test(m, col, pos):
#     for v in m:
#         index1 = 0
#         if v[0] == col:
#             index = 0
#             for v1 in v:
#                 if v1 == pos:
#                     m[index1] = "X"
#                 index += 1
#
#         index1 += 1


def fib_loop_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_loop_while(n):
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a




print(fib_loop_while(16), end=' ')


# def fib_recur(n):
#     assert n >= 0, "n > 0"
#     if n <= 1:
#         return n
#     return fib_recur(n-1) + fib_recur(n-2)
#
# print(fib_recur(16), end=' ')