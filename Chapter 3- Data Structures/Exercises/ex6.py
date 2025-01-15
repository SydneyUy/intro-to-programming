People = ['Laios','Senshi','Kabru']

print ('hello', (People[0]), 'You are invited to attend this dinner.')
print ('hello', (People[1]),'You are invited to attend this dinner.')
print ('hello', (People[2]), 'You are invited to attend this dinner.')

del(People[2])
People.insert(2,'Marcille')

print ('hello', (People[2]), 'You are invited to attend this dinner.')
print ('Kabru cannot make it to the event.')

print ('\nI can only invite 2 people now.')

People.pop()
print ('The people invited now are', People)