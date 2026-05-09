
catalogo_libros = []



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

    def obtener_datos(self):
        lista = [self.nombre, self.fecha, self.autor, self.tipo]
        return lista

class Revista(Nombre, Fecha):

    def __init__(self, nombre, fecha):
        Nombre.__init__(self, nombre)
        Fecha.__init__(self, fecha)
        self.tipo = "Revista"

    def obtener_datos(self):
        lista = [self.nombre, self.fecha, self.tipo]
        return lista

class Articulo(Nombre, Autor):

    def __init__(self, nombre, autor):
        Nombre.__init__(self, nombre)
        Autor.__init__(self, autor)
        self.tipo = "Articulo"

    def obtener_datos(self):
        lista = [self.nombre, self.autor, self.tipo]
        return lista

def ver_catalogo():
    if catalogo_libros == []:
        print("Catalogo sin obras")
    else:
        for x in catalogo_libros:
            print(x)

def anadir_obra_al_catalogo(objeto):
        nuevo_libro = repr(objeto)
        catalogo_libros.append(nuevo_libro)


def rellenar_datos_nueva_obra(tipo):
    if tipo == 1:
        nombre = input("Introduzca el nombre del libro: ")
        while True:
            try:
                fecha = int(input("Fecha de Creacion: "))
                break
            except:
                print("Debe ser un numero!")
                continue

        autor = input("Nombre del Autor: ")
        return [nombre,fecha,autor]

    elif tipo == 2:
        nombre = input("Introduzca el nombre del libro: ")
        while True:
            try:
                fecha = int(input("Fecha de Creacion: "))
                break
            except:
                print("Debe ser un numero!")
                continue
        return [nombre,fecha]

    elif tipo == 3:

        nombre = input("Introduzca el nombre del libro: ")
        autor = input("Nombre del Autor: ")
        return [nombre,autor]



