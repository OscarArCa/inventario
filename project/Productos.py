class Producto:
    
    def __init__(self, id, nombre, precio):
        self._id = id
        self._nombre = nombre
        self._precio = precio
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

    @property
    def igv(self):
        return self._precio * 0.18  

    @property
    def subtotal(self):
        return self._precio - self.igv

    @property
    def precioneto(self):
        return self._precio + self.igv
