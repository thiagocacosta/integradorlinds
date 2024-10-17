def menu():
    while True:
        print('\n'
            '[1] - Create\n'
            '[2] - Read\n'
            '[3] - Update\n'
            '[4] - Delete\n'
            '[5] - Exit\n'
            )
        op = int(input('Escolha a opção: '))
        match op:
            case 1:
                print('1')
            case 2:
                print('2')
            case 3:
                print('3')
            case 4:
                print('4')
            case 5:
                break
            

menu()