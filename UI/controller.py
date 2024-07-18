import flet as ft

from model.model import Model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        nN, nE = self._model.getGraphDetails()
        self._view._txt_result.controls.append(ft.Text(f"il grafo possiede {nN} nodi"
                                                       f" e {nE} archi"))
        self._view.update_page()
    def handleCompConnessa(self,e):
        self._view._txt_result.controls.clear()
        idAdded = self._view._txtIdOggetto.value
        if idAdded == "":
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore"))
            self._view.update_page()
            return
        try:
            intIdAdded = int(idAdded)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text(f"Inserire un valore intero"))
            self._view.update_page()
            return
        # scrivere questa forma più breve e brutale equivale
        # a scrivere if ... == True
        if self._model.checkExistence(intIdAdded):
            self._view._txt_result.controls.append(
                ft.Text(f"L'oggetto {intIdAdded} è presente nel grafo"))
        else:
            self._view._txt_result.controls.append(
                ft.Text(f"L'oggetto {intIdAdded}  NON è presente nel grafo"))


        self._view.update_page()







