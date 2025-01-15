sandwich_orders = { 'Order1': 'Cheese Sandwich', 'Order2': 'Tuna Sandwich', 
                   'Order3': 'Ham Sandwich',  'UNAVAILABLE': 'Pastrami', 
                  'UNAVAILABLE1': 'Pastrami',  'UNAVAILABLE2': 'Pastrami'}

# Finished sandwiches should be empty
finished_sandwiches = []



to_remove = []
for order, sandwich in sandwich_orders.items():
    if sandwich.lower() == 'pastrami':
        to_remove.append(order)
#Adding pastrami to a diffrent list

for order in to_remove:
    del sandwich_orders[order]
# Order = UNAVALIBLE, this will remove the pastirami and esures the code will run, without having a runtime error


while sandwich_orders:
    order, sandwich = sandwich_orders.popitem()
    print(f"I made a {sandwich}")
    finished_sandwiches.append((order, sandwich))
#Process the remaining sandwiches


print("\nAll sandwiches are finished:")
for order, sandwich in finished_sandwiches:
    print(f"{order} ({sandwich}) is done")
