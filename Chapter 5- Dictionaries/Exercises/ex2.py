glossary = {'variable':'variables are used to store data, the foundation of a program'
           ,'print':'Print functions are used to show the input when running a program',
           'comment':'# will be ignored in a program, it can be helpful for notes',
           '[]':'use square brackets [] if you want to make changes to a list',
           '()':'tuples are used for unchangable list, calling functions and grouping variables'}

#.title() makes sure the first letter is capital
word = 'variable'
print (f"\n{word.title()}:{glossary[word]}")

word = 'print'
print (f"\n{word.title()}:{glossary[word]}")

word = 'comment'
print (f"\n{word.title()}:{glossary[word]}")

word = '[]'
print (f"\n{word.title()}:{glossary[word]}")

word = '()'
print (f"\n{word.title()}:{glossary[word]}")