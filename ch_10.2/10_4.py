def collectNamesFromCL():
    flag = False

    while not flag:
        name = input('What your name?')
        print('Hello,',name,'welcome!')
        with open('guest_list.txt', 'a') as file:
            name+='\n'
            file.write(name)
        char = input('Type q and press q to quit, otherwise press enter to continue: ')
        if char == 'q':
            flag = True

collectNamesFromCL()
