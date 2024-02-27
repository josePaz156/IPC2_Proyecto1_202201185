class tipo_piso:
    def __init__(self, R, C, F, S, patrones):
        self.R = R
        self.C = C
        self.F = F
        self.S = S
        self.patrones = patrones

    def __str__(self):
        return f"R: {self.R}, C: {self.C}, F: {self.F}, S: {self.S}, patrones: {self.patrones}"
