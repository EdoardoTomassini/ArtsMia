import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._artObjectList = DAO.getObjects()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        # Un dizionario è tale e quale ad una treemap
        # su Java
        # ----> Associo ad un elemento del dizionario contraddistinto
        # da un indice un oggetto, in questo caso un ArtObject
        for v in self._artObjectList:
            self._idMap[v.object_id] = v
        # questo idMap devo poi passarlo al DAO


    def buildGraph(self):
        self.addEdges()

    def addEdges(self):
        # dà problemi
        #self._grafo.edges.clear()

        allEdges = DAO.getAllConnessioni(self._idMap)

        #ciclo sulla lista di oggetti Connessione allEdges per aggiungere i nodi al grafo
        for edge in allEdges:
            self._grafo.add_edge(edge.v1, edge.v2, weight = edge.peso)




    def getObjects(self):
        return DAO.getObjects()

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getEdges(self):
        edges = DAO.getAllConnessioni()

    def checkExistence(self, idOggetto):
        # verifica se il parametro passato al metodo
        # in questo caso idMap è contenuto tra gli
        # indici del dizionario idMap (chiavi per treeMap)
        # restituisce True o False
        return idOggetto in self._idMap
