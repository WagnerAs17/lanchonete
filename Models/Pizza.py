class Pizza:

    def __init__(self, molho, recheio, borda):
        self.molho = molho
        self.recheio = recheio
        self.borda = borda

    def __str__(self):
        return f"Pizza - Molho: {self.molho} / Recheio: {self.recheio} / Borda: {'Sim' if self.borda else 'Não'}"