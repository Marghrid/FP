class garrafa:
    def __init__(self, cap):
        self.niv = 0
        self.cap = cap
    
    def capacidade (self):
        return self.cap
    
    def nivel(self):
        return self.niv
    
    def despeja (self, qt):
        if self.niv - qt < 0:
            self.niv = 0
        else:
            self.niv = self.niv - qt
        return self.niv

    def enche (self, qt):
        if self.niv + qt > self.cap:
            self.niv = self.cap
        else:
            self.niv = self.niv + qt
        return self.niv