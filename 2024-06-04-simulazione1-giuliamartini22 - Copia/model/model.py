import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listYears = []
        self.listShapes = []
        self._idMap = {}
        self._grafo = nx.Graph()
        self._nodi = []
        # andrea
        self.listStates = []
        self._listCapitali = []
        # fine andrea
        self._idMapName = {}
        self._listSighting = []
        self._idMapSighting = {}
        self._grafoSighting = nx.Graph()
        self._idMapPopulation = {}
        self._grafoPopulation = nx.Graph()
        self._nodiDuration = []
        self._grafoDuration = nx.Graph()

    def buildGraph(self, anno, shape):
        self._nodi = DAO.getAllStates()

        for s in self._nodi:
            self._idMap[s.id] = s

        for s in self._nodi:
            self._idMapName[s.Name] = s
            #print(self._idMapName[s.id], self._idMapName[s.id].value)
        print(self._idMapName.keys(), self._idMapName.values())

        self._grafo.add_nodes_from(self._nodi)

        self._archi = DAO.getAllEdges(self._idMap)
        for e in self._archi:
            st1 = e.s1
            st2 = e.s2
            peso = DAO.getPesi(anno,shape, st1.id, st2.id)
            if peso > 0:
                self._grafo.add_edge(st1, st2, weight = peso)
                print(st1.id, st2.id, peso)

    def buildGraphDuration(self, durata):
        self._nodiDuration = DAO.getAllSightingwithDuration(durata)

        self._grafoDuration.add_nodes_from(self._nodiDuration)

    def getAllVicini(self):
        elencoPesiVicini = []
        for s in self._grafo.nodes():
            peso = self.getPesoVicini(s)
            elencoPesiVicini.append((s.id,peso))
        return elencoPesiVicini

    def getPesoVicini(self, v0):
        vicini = self._grafo.neighbors(v0)
        pesoTot = 0
        for v in vicini:
            pesoTot += self.getEdgeWeight(v0, v)
        return pesoTot

    def getEdgeWeight(self, v0, v):
        return self._grafo[v0][v]['weight']

    def getYears(self):
        self._listYears = DAO.getYears()
        return self._listYears

    def getShapes(self):
        self._listShapes = DAO.getShapes()
        return self._listShapes

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    # andrea
    def getStates(self):
        self._listStates = DAO.getAllStatesAndrea()
        return self._listStates
    # fine andrea
    def getCapitali(self):
        self._listCapitali = DAO.getAllCapitali()
        return self._listCapitali
    # fine andrea

    def creagrafoSighting(self):
        self._grafoSighting.clear()
        self._nodiSighting = DAO.getAllSighting()
        for s in self._nodiSighting:
            self._idMapSighting[s.id] = s

        self._grafoSighting.add_nodes_from(self._nodiSighting)

    def getNumNodiSighting(self):
        return len(self._grafoSighting.nodes)

    def getNumArchiSighting(self):
        return len(self._grafoSighting.edges)

    def creaGrafoPopulation(self, soglia):
        self._grafoPopulation.clear()
        self._nodiStatePopulation = DAO.getAllStatesPopulation(soglia)
        for s in self._nodiStatePopulation:
            self._idMapPopulation[s.id] = s

        self._grafoPopulation.add_nodes_from(self._nodiStatePopulation)

    def getNumNodiPopulation(self):
        return len(self._grafoPopulation.nodes)

    def getNumArchiPopulation(self):
        return len(self._grafoPopulation.edges)

    def getCodiceStato(self, stato):
        return DAO.getCodiceStato(stato)

    #def getAllSighting(self):
    #    self._listSighting = DAO.getAllSighting()
    #    return self._listSighting