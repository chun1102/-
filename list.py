mathScores = [60, 70, 10, 20, 81, 63, 4]

print(mathScores[3])
print(mathScores[2:6])
print(mathScores[-1])
print(mathScores[:5])
print(mathScores[5:])
print(mathScores[-6:])
print(len(mathScores))
print(sum(mathScores))
print(max(mathScores))
print(min(mathScores))
s = sum(mathScores)
l = len(mathScores)
print(s / l)
# -------------------------------------

ls = []
ls.append(4)
print(ls)
ls.insert(0, 10)
print(ls)

mathScores = [10, 4, 56, 44, 89, 66, 53, 97]

del mathScores [1:3]
print(mathScores)
mathScores.remove(66)
print(mathScores)

mathScores[2] = 1
print(mathScores)

print(2 in mathScores)
print(10 in mathScores)
print(mathScores.count(10))

ls1 = ['a', 'b', 'c']
print(mathScores + ls1)

# ----------------------------------------

ls2 = [[1, 3], [6, 3]]
print(ls2[1][0])

print(sorted(mathScores))


