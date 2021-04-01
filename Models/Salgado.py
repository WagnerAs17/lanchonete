class Salgado:

    def __init__(self, recheio, massa):
        self.recheio = recheio
        self.massa = massa

    def __str__(self):
        return f"Salgado - Recheio: {self.recheio} / Massa: {self.massa}"