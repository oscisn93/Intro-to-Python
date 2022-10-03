from time import process_time_ns


def store_car(manufacturer, model, **args):
    args['manufacturer'] = manufacturer
    args['model'] = model
    return args

print(store_car('ford', 'focus', runs=False, value=-200))