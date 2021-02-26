import sqlite3 as sql
from Modelos.Persona import Persona


class TermometroDAO:
    __con = sql.connect('database.db')
    __cur = __con.cursor()

    def __init__(self):
        self.__cur.execute(
            'CREATE TABLE IF NOT EXISTS Termometro(id_persona INTEGER, temperatura VARCHAR(30) NOT NULL, fecha VARCHAR(30) NOT NULL, CONSTRAINT fk_id_persona FOREIGN KEY(id_persona) REFERENCES Persona(id_persona));')
        self.__con.commit()

    def add(self, persona: Persona, temperatura: str, fecha: str):
        self.__cur.executemany('INSERT INTO Termometro(id_persona, temperatura, fecha) VALUES(?,?,?);',
                               [(persona.id, temperatura, fecha)])
        self.__con.commit()

    def get_temperatura(self, id_persona: int):
        """
            Retorna la temperatura de una persona
        :param id_persona:
        :return:
        """
        self.__cur.execute(f'SELECT * FROM Termometro WHERE id_persona = "{id_persona}";')
        return self.__cur.fetchall()

    def get_all(self):
        """
            Retorna todas las personas cargadas en la bd
        :return:
        """
        self.__cur.execute('SELECT * FROM Termometro;')
        return self.__cur.fetchall()

    def get_temperatura_persona(self, id_persona: int):
        query = f'SELECT t.temperatura, t.fecha FROM Termometro as t INNER JOIN Persona as p ON p.id_persona = t.id_persona WHERE t.id_persona = {id_persona};'
        self.__cur.execute(query)
        return self.__cur.fetchall()
