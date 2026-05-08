class Nombre:
    def __init__(self,nombre):
        self.nombre = nombre
class Fecha:
    def __init__(self,fecha):
        self.fecha = fecha
class Autor:
    def __init__(self,autor):
        self.autor = autor

class Libro(Nombre, Fecha, Autor):

    def __init__(self, nombre, fecha, autor):
        Nombre.__init__(self, nombre)
        Fecha.__init__(self, fecha)
        Autor.__init__(self, autor)
        self.tipo = "Libro"

class Revista(Nombre, Fecha):

    def __init__(self, nombre, fecha, autor):
        Nombre.__init__(self, nombre)
        Fecha.__init__(self, fecha)
        self.tipo = "Revista"

class Articulo(Nombre, Autor):

    def __init__(self, nombre, fecha, autor):
        Nombre.__init__(self, nombre)
        Autor.__init__(self, autor)
        self.tipo = "Articulo"

class Catalogo:
    def __init__(self):
        pass
    def ver_catalogo(self):

        return NotImplementedError
    def añadir_obra_al_catalogo(self):
        pass



