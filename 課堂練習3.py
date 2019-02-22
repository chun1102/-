gradesDict = {'chinese': [5, 14, 7], 'english': [23, 36, 28], 'math': [88, 80, 92]}

print(gradesDict['math'])

chineseavg = sum(gradesDict['chinese'])/len(gradesDict['chinese'])
englishavg = sum(gradesDict['english'])/len(gradesDict['english'])
mathavg = sum(gradesDict['math'])/len(gradesDict['math'])
print('國文平均:', chineseavg,'英文平均:', englishavg,'數學平均:', mathavg)

gradesDict.update({'science': [94, 90, 96]})
print(gradesDict)

