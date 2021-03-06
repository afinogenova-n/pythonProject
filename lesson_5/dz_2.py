
n = int(input('Введите число: '))

num_gen = (num for num in range(1, n+1, 2))

for i in range(1, n+3, 2):
    print(next(num_gen))