sandwhich_orders = ["pastrami", "meatball", "peanut butter and jelly"]
finished_sandwhiches =[]

while len(sandwhich_orders) > 0:
    order = sandwhich_orders[0]
    msg = f"I finshed your {order} sandwhich."
    print(msg)
    finished_sandwhiches.append(order)
    sandwhich_orders.pop(0)
