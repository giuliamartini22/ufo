import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
        self._shape = None
        self._anno = None
        # giulia
        self._listState = []
        self._state = None
        self._capitale = None
        self._listCapitali = []
        # fine giulia

    def fillDD(self):
        self._listShape = self._model.getShapes()
        #print(self._listCountry)
        for c in self._listShape:
            self._view.ddshape.options.append(ft.dropdown.Option(c[0]))
        self._view.update_page()

    def read_shape(self, e):
        if e.control.value == "None":
            self._shape = None
        else:
            self._shape = e.control.value

    # giulia
    def fillDDandrea(self):
        self._listState = self._model.getStates()
        for s in self._listState:
            self._view.ddstate.options.append(ft.dropdown.Option(s))
        self._view.update_page()
    # fine

    # giulia
    def read_state(self, e):
        if e.control.value == "None":
            self._state = None
        else:
            self._state = e.control.value
        print(self._state)
    # fine
        # giulia
    def fillDDCapitali(self):
        self._listCapitali = self._model.getCapitali()
        for s in self._listCapitali:
            self._view.ddcapitali.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    # fine

    # giulia
    def read_capitali(self, e):
        if e.control.value == "None":
            self._capitale = None
        else:
            self._capitale = e.control.value
    # fine

    #andrea
    def handle_controlloandrea(self, e):
        # NameStato = self._view.ddstate.value
        NameStato = self._state
        if NameStato is None:
            self._view.create_alert("Stato non selezionato")
            return
        # controllo e gestione del valore soglia
        try:
            numeroandrea = int(self._view._txtNumeroAndrea.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Numero Andrea Non Inserito"))
            self._view.update_page()
            return

        codiceStato = self._model.getCodiceStato(NameStato)
        print(codiceStato)
        self._view.txt_result.controls.append(ft.Text(codiceStato))
        self._model.creagrafoSighting()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato, num vertici {self._model.getNumNodiSighting()}"))
        self._model.creaGrafoPopulation(numeroandrea)
        self._view.txt_result.controls.append(ft.Text(f"Grafo popolazione correttamente creato, num vertici {self._model.getNumNodiPopulation()}"))
        self._view.update_page()
    #fine andrea

    def populate_dd_anno(self):
        """methodo che popola la tendina con tutti gli anni in cui ci sono state vendite,
        prendendo le informazioni dal database"""
        self._listYear = self._model.getYears()
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        """event handler che legge l'anno scelto dal menu a tendina ogniqualvolta viene cambiata
        la scelta, e lo memorizza in una variabile di instanza. L'anno è un intero, se si tratta di un anno,
        oppure un None se viene scelta l'opzione nessun filtro sull'anno"""
        if e.control.value == "None":
            self._anno = None
        else:
            self._anno = e.control.value

    def handle_graph(self, e):
        #anno = self._view.ddyear.value
        #shape = self._view.ddshape.value
        #print(anno)
        #try:
        #    annoIns = int(anno)
        #except ValueError:
        #    self._view.txt_result.controls.clear()
        #    self._view.txt_result.controls.append(ft.Text("Anno non inserito"))
        #    self._view.update_page()
        #    return
        anno = self._anno
        shape = self._shape
        if anno is None:
            self._view.create_alert("Anno non inserito")
            return
        if shape is None:
            self._view.create_alert("Shape non inserita")
            return

        print(shape)
        #try:
        #    shapeIns = str(shape)
        #except ValueError:
        #    self._view.txt_result.controls.append(ft.Text("Shape non inserita"))
        #    self._view.update_page()
        #    return
        if shape is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Shape non inserita"))
            return


        self._model.buildGraph(anno, shape)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))
        allVicini = self._model.getAllVicini()
        for v in allVicini:
            self._view.txt_result.controls.append(ft.Text(f"{v[0]} ha peso {v[1]}"))
        self._view.update_page()

    def handle_path(self, e):
        pass