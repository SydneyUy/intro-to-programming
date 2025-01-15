sandwich_orders = {'Order1':'Cheese Sandwhich', 'Order2' : 'Tuna Sandwhich', 
                   'Order3': 'Ham Sandwhich'}

# Finished sandwiches should be empty
finished_sandwiches = []

while sandwich_orders:
    order, sandwich = sandwich_orders.popitem()
    print(f"I made a {sandwich}")
    finished_sandwiches.append((order, sandwich))

print("\nAll sandwiches are finished:")
for order, sandwich in finished_sandwiches:
    print(f"{order} ({sandwich}) is done")


