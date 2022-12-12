from Restaurant import Restaurant

class iceCreamStand(Restaurant):
    def __init__(self, name, ctype, flavors):
        Restaurant.__init__(self, name, ctype)
        self.flavors = flavors
    
    def print_flavors(self):
        n = len(self.flavors)
        switch = [
            self.flavors[0],
            f'{self.flavors[0]} and {self.flavors[1]}',
        ]
        if n < 3:
            if  n < 1:
                print('The',self.ctype,'Sorry the shop is all out of flavors')
                return
            flavor_str = switch.get(n-1)
        else:
            flavor_str = ''
            index = 0
            for flavor in self.flavors:
                if index == (n - 1):
                    flavor_str += f'and {flavor}'
                else:
                    flavor_str += f'{flavor}, '
                index += 1
        print('This shop has the flavors:',flavor_str)
        
flavors = ['chocolate', 'vanilla', 'sherbert']
bobs = iceCreamStand('Bill\'s', 'ice cream', flavors)
bobs.print_flavors()