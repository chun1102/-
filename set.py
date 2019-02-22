fruits = {'apple', 'banana', 'guava', 'guava'}
print(len(fruits))
print('pineapple' in fruits)

fruits1 = {'strawberry', 'papaya', 'banana'}
print(fruits | fruits1)

# 課堂練習
allStudents = {'John', 'Eva', 'Jill', 'Eric',
               'Andy', 'Albert', 'Polina', 'Kristin', 'Angela'}
GuitarClub = {'John', 'Eva', 'Jill', 'Eric', 'Andy'}
DanceClub = {'Andy', 'Eric', 'Albert', 'Polina', 'Kristin'}

print(GuitarClub & DanceClub)
print(GuitarClub - (GuitarClub & DanceClub))
print(allStudents - (GuitarClub | DanceClub))

