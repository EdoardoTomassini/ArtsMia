from database.DB_connect import DBConnect
from model.Connessione import Connessione
from model.artObject import ArtObject


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    select * from objects o
                """

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT eo1.object_id as o1, eo2.object_id as o2, COUNT(*) as peso
                    FROM exhibition_objects eo1, exhibition_objects eo2 
                    WHERE eo1.exhibition_id = eo2.exhibition_id 
                    and eo1.object_id < eo2.object_id
                    GROUP by eo1.object_id, eo2.object_id 
                    order by peso desc
                    """

        cursor.execute(query, ())

        for row in cursor:
            result.append(Connessione(idMap[row["o1"]],
                                      idMap[row["o2"]],
                                      row["peso"]
                                      ))

        cursor.close()
        conn.close()
        return result