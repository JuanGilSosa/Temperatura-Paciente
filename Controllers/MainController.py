from DAO.TermometroDAO  import TermometroDAO
from DAO.PersonaDAO     import PersonaDAO
from Modelos.Persona    import Persona
from Modelos.Termometro import Termometro
from os                 import system
from tabulate           import tabulate

import time
import Vista.Menu as Menu

dao_persona = PersonaDAO()
dao_termometro = TermometroDAO()

def start():
    op = 1
    while op in [1, 2, 3]:
        op = Menu.menu()
        if op == 1:
            system('cls')
            print('******************CARGA AL SISTEMA******************')
            name = input('| Ingrese nombre.................: ')
            temp = input('| Ingrese temperatura corporal...: ')
            temp = temp + '°'
            
            persona = Persona(name)
            if not dao_persona.exists(persona.nombre):
                dao_persona.add(persona)

            persona.id = dao_persona.get_id_by_name(persona.nombre)

            termometro = Termometro(temp, time.strftime("%x") + " | " + time.strftime("%X"), persona.id)
            dao_termometro.add(persona, termometro.temperatura, termometro.fecha)

            system('cls')

        elif op == 2:
            system('cls')
            print('******************CARGA AL SISTEMA******************')
            name = input('| Ingrese nombre.................: ')
            temp = input('| Ingrese temperatura corporal...: ')
            temp = temp + '°'
            hora = input('| Ingrese la hora (HH-MM-SS).....: ')

            persona = Persona(name)
            if not dao_persona.exists(persona.nombre):
                dao_persona.add(persona)

            persona.id = dao_persona.get_id_by_name(persona.nombre)

            termometro = Termometro(temp, time.strftime("%x") + " | " + hora, persona.id)
            dao_termometro.add(persona, termometro.temperatura, termometro.fecha)

            system('cls')

        elif op == 3:
            system('cls')
            name = input('| Ingrese nombre.................: ')
            if not dao_persona.exists(name):
                print('|| Ese no existe! cargue en el sistema sus temperaturas ||')
                system('pause')
                system('cls')
            else:
                system('cls')
                id_persona = dao_persona.get_id_by_name(name)
                lista = dao_termometro.get_temperatura_persona(id_persona)
                print(tabulate(lista, headers=['Temperatura', 'Fecha'], showindex=True), end='\n')
                system('pause')
                system('cls')
