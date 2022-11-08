def collectReasonsFromCL():
    flag = False

    while not flag:
        reason = input('Why do you love programming?')
        with open('reason_list.txt', 'a') as file:
            reason+='\n'
            file.write(reason)
        char = input('Type q and press q to quit, otherwise press enter to continue: ')
        if char == 'q':
            flag = True

collectReasonsFromCL()