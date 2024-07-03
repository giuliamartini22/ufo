from flet_core import row

from database.DB_connect import DBConnect
from model.Sighting import Sighting
from model.edge import Edge
from model.state import State


class DAO():
    @staticmethod
    def getYears() -> list[tuple[int]] | None:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """select distinct YEAR(s.`datetime`)
                        from sighting s """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def getShapes() -> list[tuple[str]]:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """select distinct s.shape 
                        from sighting s """
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore di connessione")
            return None

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s"""

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCapitali():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Capital
                        from state s"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["Capital"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.state1, n.state2
                    from neighbor n   """

        cursor.execute(query)

        for row in cursor:
            result.append(Edge(idMap[row["state1"]], idMap[row["state2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPesi(year, shape, stato1, stato2):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor()
        query = """select count(*) as peso
                    from sighting s 
                    where s.shape = %s
                    and Year(s.`datetime`) = %s
                    and (s.state = %s or s.state = %s)"""

        cursor.execute(query, (shape, year, stato1, stato2))

        result = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        return result

    # andrea
    @staticmethod
    def getAllStatesAndrea():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select Name
                    from state s"""

        cursor.execute(query)
        # rows = cursor.fetchall()
        for row in cursor:
            result.append(row["Name"])

        cursor.close()
        conn.close()
        return result
        # return rows
    # fine andrea

    @staticmethod
    def getCodiceStato(stato):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor()
        query = """select id as idStato
                        from state s 
                        where s.Name = %s"""

        cursor.execute(query, (stato,))

        result = cursor.fetchone()[0]

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllSighting():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                        from sighting s"""

        cursor.execute(query)

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStatesPopulation(valore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                        from state s
                        where s.Population > %s"""

        cursor.execute(query, (valore,))

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllSightingwithDuration(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from sighting s 
                    where s.duration > %s"""

        cursor.execute(query, (durata,))

        for row in cursor:
            result.append(Sighting(**row))

        cursor.close()
        conn.close()
        return result
