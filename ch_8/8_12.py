def print_sandwhich(*args):
    if len(args) > 1:
        msg = "The sandwhich is made of "
        count = 0
        for arg in args:
            if count == (len(args) - 1):
                msg += f"and {arg}."
            else:
                msg += f"{arg}, "
            count += 1
    else:
        msg = f"The sandwhich is made of {args[0]}."
    print(msg)


print_sandwhich("peanut butter")
print_sandwhich("peanut butter", "jelly")
print_sandwhich("ham", "mayonaise", "tomatoes", "lettuce", "cheese")
