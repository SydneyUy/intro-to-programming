#yangtze:China Amazon:Brazil Nile:ethiopia
River = {'nile':'ethiopia','Amazon' : 'Brazil','yangtze':'China'}
for Country in River.values():

    print (f'\n{Country}')


for River, Country in River.items():
    print(f"\n The {River.title()} river goes through: {Country}")

    
for River in River.keys():
    print (f'\n{River}')

    