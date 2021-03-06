# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

n = int(input('Введите число: '))
def gen_gen(n):
    for num in range(1, n+1, 2):
        yield num



num_gen = gen_gen(n)

for i in range(1, n+3, 2):
    print(next(num_gen))


