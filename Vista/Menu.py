from os import system


def menu() -> int:
    print('**************************************')
    print('*******Bienvenidos al asistente*******')
    print('**************************************\n')
    print('[1] - Cargar Temperatura')
    print('[2] - Ver temperatura')
    print('[3] - Salir')
    op = int(input('Elija una opción...: '))
    system('cls')
    return op
