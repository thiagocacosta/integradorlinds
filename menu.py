import subprocess

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
                subprocess.run(["python", "create.py"])  # Substitua 'create.py' pelo nome do seu arquivo
            case 2:
                subprocess.run(["python", "read.py"])  # Substitua 'read.py' pelo nome do seu arquivo
            case 3:
                subprocess.run(["python", "update.py"])  # Substitua 'update.py' pelo nome do seu arquivo
            case 4:
                subprocess.run(["python", "delete.py"])  # Substitua 'delete.py' pelo nome do seu arquivo
            case 5:
                break
            

menu()