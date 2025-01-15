#Main list of pets
pets = []

#In each dictionary, include the kind of animal and the owner’s name.
pet = {'Owner_name': 'Lily',
             'Pet':'Dog',  
              'age_pet':'5 years old',     
              'Fav_food':'Beef'}

#adding the pets in the main list
pets.append(pet)

pet = {'Owner_name': 'Ken',
             'Pet':'Cat',  
              'age_pet':'1 year old',     
              'Fav_food':'Cardboard'}

pets.append(pet)

pet = {'Owner_name': 'Ryan',
             'Pet':'Sugar glider',  
              'age_pet':'3 months old',     
              'Fav_food':'Peanuts'}

pets.append(pet)


for pet in pets:
        print("\t", str(pet))