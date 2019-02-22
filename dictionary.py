family = {'dad': 'Homer',
          'mom': 'Marge',
          'daughter': 'Lisa',
          'son': 'Bart'}

family['cousin'] = 'pig'
family.update({'uncle': 'Martin'})
print(family)
del family['cousin']
print(family.pop('uncle'))
print(family)
family['dad'] = 'Andy'
print(family)

