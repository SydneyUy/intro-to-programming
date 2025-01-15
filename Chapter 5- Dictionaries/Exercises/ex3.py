glossary = {'variable':'variables are used to store data, the foundation of a program'
           ,'print':'Print functions are used to show the input when running a program',
           'comment':'# will be ignored in a program, it can be helpful for notes',
           '[]':'use square brackets [] if you want to make changes to a list',
           '()':'tuples are used for unchangable list, calling functions and grouping variables',
           'Loop':'prints a group of code stated',
           'float':'a funtion that tells the program the numbers stated have a decimal place',
           'integers':'a funtion that tells the program the number stated is a whole number'}

#for this one I discarded .title()
for word, definition in glossary.items():
    print(f"\n{word}: {definition}")
