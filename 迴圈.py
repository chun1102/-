for i in range(0, 10):
    print(i)
print('1-----------------------------')
for i in range(0, 10, 2):
    print(i)
print('2-----------------------------')
mathScores = [60, 70, 10, 20, 81, 63, 4]
l = len(mathScores)
for i in range(0, l):
    print(i, mathScores[i]*10)
print('3-----------------------------')
for l, i in enumerate(mathScores):
    print(l, i)
print('3-----------------------------')
print(list(enumerate(mathScores)))
print('4-----------------------------')
for i in mathScores:
    print(i)
print([i*10 for i in mathScores])
print(list(i*10 for i in mathScores))
print('5-----------------------------')
family = {'dad': 'Homer',
          'mom': 'Lisa'}
for title, name in family.items():
    print(title, ':', name)
print('6-----------------------------')
X = (1, 2, 3)
Y = (4, 5, 6)
for x, y in zip(X, Y):
    print(x, y)
print('7-----------------------------')
count = 0
while count < 10:
    print(count)
    count += 1
else:
    print('count >= 10')
print('8-----------------------------')
for i in range(0 ,20):
   if i % 2 == 0:
       print(i)
print('9-----------------------------')
for i in mathScores:
    if i > 80:
        break
    print(i)
print('10-----------------------------')
for i in mathScores:
    if i > 80:
        continue
    print(i)