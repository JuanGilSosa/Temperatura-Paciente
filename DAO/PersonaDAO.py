import sqlite3 as sql
from Modelos.Persona import Persona


class PersonaDAO:
    __con = sql.connect('database.db')
    __cur = __con.cursor()

    def __init__(self):
        self.__cur.execute(
            'CREATE TABLE IF NOT EXISTS Persona(id_persona INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(30) NOT NULL);')
        self.__con.commit()

    def add(self, persona: Persona):
        self.__cur.execute('INSERT INTO Persona(nombre) VALUES(?);', [persona.nombre])
        self.__con.commit()

    def get_persona(self, nombre: str):
        """
            Retorna una persona, buscada por nombre
        :param nombre:
        :return:
        """
        self.__cur.execute(f'SELECT * FROM Persona as p WHERE p.nombre = "{nombre}";')
        return self.__cur.fetchall()

    def get_all(self):
        """
            Retorna todas las personas cargadas en la bd
        :return:
        """
        self.__cur.execute('SELECT * FROM Persona;')
        return self.__cur.fetchall()

    def get_last_id(self):
        """
            Retorna el ultimo id cargado de una persona
        :return:
        """
        self.__cur.execute('SELECT max(id_persona) FROM Persona;')
        return self.__cur.fetchone()

    def get_id_by_name(self, name: str):
        """
            Retorna el id de una persona cargada
        :param name:
        :return:
        """
        self.__cur.execute(f'SELECT id_persona FROM Persona WHERE nombre = "{name}";')
        return self.__cur.fetchone()[0]

    def exists(self, nombre) -> bool:
        """
            Retorna true si existe, false si no existe
        :param nombre:
        :return bool:
        """
        self.__cur.execute(f'SELECT * FROM Persona WHERE nombre = "{nombre}";')
        data = self.__cur.fetchall()
        if data:
            return True

        return False
