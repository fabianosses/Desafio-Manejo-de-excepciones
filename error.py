class DimensionError(Exception):
    def __init__(self, mensaje: str, dimension: int = None, maximo: int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension and self.maximo:
            return f"{self.mensaje} - Dimensión: {self.dimension}, Máximo permitido: {self.maximo}"
        return super().__str__()