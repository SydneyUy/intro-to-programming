while True:
    Age = int (input ('enter your age:'))
    
    if Age<=3:
      print ('the ticket is free')
    elif Age<=12:
      print ('the ticket is $10')
    elif Age>13:
      print ('the ticket is $15')
    else:
      print ('end')
      break
   

print ('continue')

