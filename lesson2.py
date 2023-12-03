
print('мы перед циклом')

print(5>3)
print(4<2)
print(4==4)
print(4!=3)

n = int(input('введите цисло больше нуля'))


while n>0:
    if n % 2 == 0:
        print('четное число', n)
    else:
        print('нечетное число')
    n = n - 1

name = 'Дмитрий'

for i in name:
    print(i)

for i in range(len(name)):
    print(i, name[i])

for j in [10,9,8,7,6,5,4,3,2,1]:
    print(j)

a = [10,9,8,7,6,5,4,3,2,1]
