class tipo_patrones:
    def __init__(self, codigo, contenido):
        self.codigo = codigo
        self.contenido = contenido
        
    def __str__(self):
        return f"Código: {self.codigo}, Contenido: {self.contenido}"