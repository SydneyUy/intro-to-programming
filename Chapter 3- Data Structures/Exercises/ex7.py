Loc = ['Sweden','Canberra','Rio de janerio','Jamaica','Manila']

print ('\nunmodified:')
print (Loc)

print ('\nAlphabetical:')
print (sorted(Loc))

print ('\nback to original:')
print (Loc)

print ('\nReverse Alphabetical:')
print (sorted(Loc,reverse=True))

print ('\nback to original:')
print (Loc)

print ('\nReverse the list(twice):')
Loc.reverse()
print (Loc)

Loc.reverse()
print (Loc)

print ('\nAlphabetical order and reverse Alphabetical:')
print (sorted(Loc))
print (sorted(Loc,reverse=True))

