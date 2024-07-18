from dataclasses import dataclass

from model.artObject import ArtObject


@dataclass
class Connessione:
    v1: ArtObject
    v2: ArtObject
    peso: int

    def __str__(self):
        return f"Arco: {self.v1} - {self.v2} - peso: {self.peso}"

    def __hash__(self):
        return hash(self.v1.object_id)