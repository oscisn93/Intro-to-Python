sandwhich_orders = ["pastrami", "pastrami", "pastrami", "meatball", "peanut butter and jelly"]
finished_sandwhiches =[]

out_of = "pastrami"
print (f"We ran out of {out_of}")

while len(sandwhich_orders) > 0:
    order = sandwhich_orders[0]
    if order != out_of:
        msg = f"I finshed your {order} sandwhich."
        print(msg)
        finished_sandwhiches.append(order)
    sandwhich_orders.pop(0)
