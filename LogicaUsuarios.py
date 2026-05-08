from abc import ABC, abstractmethod
class Nombre:
    def __init__(self,_nombre):
        self.nombre = _nombre

class Edad:
    def __init__(self,_edad):
        self.edad = _edad

class Gmail:
    def __init__(self, _gmail):
        self.gmail = _gmail

class Password:
    def __init__(self, _passw):
        self.passw = _passw

class Usuario(ABC,Nombre,Edad,Gmail,Password):
    @classmethod
    @abstractmethod

    def __init__(self,_nombre,_edad,_gmail,_password):

        Nombre.__init__(self,_nombre)
        Edad.__init__(self,_edad)
        Gmail.__init__(self,_gmail)
        Password.__init__(self,_password)
        self.estado_cuenta = NotImplemented

    @property
    def obtener_estado(self):
        return self.estado_cuenta

    @property
    def obtener_password(self):
        return self.__pass

    def ver_permisos(self):
        pass

class PermisoLectura:
    def __init__(self,estado_cuenta):
        self.estado = estado_cuenta

    def permiso_lectura(self):
        pass

class PermisoVisualizar:
    def __init__(self,estado_cuenta):
        self.estado = estado_cuenta

    def permiso_visualizar(self):
        return "s"

class PermisoAdministrativo:

    def __init__(self,estado_cuenta):
        self.estado = estado_cuenta

    def permiso_administrativos(self):
        pass

class Lector(Usuario, PermisoLectura, PermisoVisualizar):
     def __init__(self,_nombre,_edad,_gmail,_password):
         super().__init__(_nombre,_edad,_gmail,_password)

         self.estado_cuenta = "Lector"


class Invitado(Usuario, PermisoVisualizar):
    def __init__(self,_nombre,_edad,_gmail,_password):
         super().__init__(_nombre,_edad,_gmail,_password)

         self.estado_cuenta = "Invitado"



class Admin(Usuario, PermisoAdministrativo, PermisoLectura, PermisoVisualizar):

     def __init__(self,_nombre,_edad,_gmail,_password):
         super().__init__(_nombre,_edad,_gmail,_password)

         self.estado_cuenta = "Administrador"
