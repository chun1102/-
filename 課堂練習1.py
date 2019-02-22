chinese = [5, 14, 7]
english = [23, 36, 28]
math = [88, 80, 92]

grades = [chinese, english, math]

print('數學成績:',grades[2])    # 數學成績
print('國文成績平均:', sum(grades[0])/len(grades[0]))   # 國文成績平均
print('英文成績平均:', sum(grades[1])/len(grades[1]))   # 英文成績平均
print('數學成績平均:', sum(grades[2])/len(grades[2]))   # 數學成績平均

naturl = [94, 90, 96]
grades.append(naturl)
print(grades)

