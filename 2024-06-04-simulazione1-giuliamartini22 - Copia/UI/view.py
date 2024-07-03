import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddyear = None
        self.ddshape = None
        self.btn_graph = None
        self.txt_result = None
        self.txt_container = None

        self.txtN = None
        self.txtOut2 = None
        self.btn_path = None

        #definizione dd stato
        self.ddstate = None
        self.ddcapitali = None


    def load_interface(self):
        # title
        self._title = ft.Text("Lab13 - Ufo sighting", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self.ddyear = ft.Dropdown(label="Anno", options=[ft.dropdown.Option(key="None",
                                                            text="Nessun filtro")],
                                                            on_change=self._controller.read_anno)
        self.ddshape = ft.Dropdown(label="Shape", options=[ft.dropdown.Option(key="None",
                                                            text="Nessun filtro")],
                                                            on_change=self._controller.read_shape)


        # button for the "creat graph" reply
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self.ddyear,self.ddshape, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._controller.fillDD()
        self._controller.populate_dd_anno()



        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

        self.btn_path = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_path)

        row2 = ft.Row([self.btn_path],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # inizio giulia
        # inserito dropdown
        self.ddstate = ft.Dropdown(label="State", options=[ft.dropdown.Option(key="None",
                                                                              text="Nessun filtro")],
                                   on_change=self._controller.read_state)
        self.ddcapitali = ft.Dropdown(label="Capitali", options=[ft.dropdown.Option(key="None",
                                                                              text="Nessun filtro")],
                                   on_change=self._controller.read_capitali)
        # inserito numero
        self._txtNumeroAndrea = ft.TextField(label="Numero da inserire",
                                             width=150)
        # inserito bottone
        self.btn_controlloandrea = ft.ElevatedButton(text="Controllo Andrea",
                                                     on_click=self._controller.handle_controlloandrea)

        row2 = ft.Row([self.ddstate, self.ddcapitali, self._txtNumeroAndrea, self.btn_controlloandrea],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._controller.fillDDandrea()
        self._controller.fillDDCapitali()

        # fine giulia

        self.txtOut2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txtOut2)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
