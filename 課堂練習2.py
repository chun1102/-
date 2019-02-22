
gradesTuple = (5, 14, 7), (23, 36, 28), (88, 80, 92)
print(gradesTuple)
print('數學成績:', gradesTuple[2])

print('國文成績平均:', sum(gradesTuple[0])/len(gradesTuple[0]))   # 國文成績平均
print('英文成績平均:', sum(gradesTuple[1])/len(gradesTuple[1]))   # 英文成績平均
print('數學成績平均:', sum(gradesTuple[2])/len(gradesTuple[2]))   # 數學成績平均

naturl = (94, 90, 96)
gradesTuple+=((94, 90, 96),)
print(gradesTuple)

tuple3 = (1,)
print(tuple3)