print ("A girl heads to a computer shop to buy some USB sticks.\nShe loves USB sticks and wants as many as she can get for £50.\nThey are £6 each.")
print ("\nhow many USB sticks she can buy? and how many pounds she will have left?")

money = 50
USB_Price= 6

Buy = money // USB_Price
left = money % USB_Price

print ("\nThe girl can Buy", Buy, "USB sticks with £50.")
print ("The girl has £", left, "leftover.\n")