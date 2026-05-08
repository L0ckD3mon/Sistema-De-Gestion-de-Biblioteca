from LogicaUsuarios import Nombre,Password,Gmail,Edad
from Usuarios import  usuarios

class Verificador(Password,Nombre):
    def __init__(self,_nombre,_passw):
        Nombre.__init__(self, _nombre)
        Password.__init__(self, _passw)

    def verificar_nombre(self):
        for x in usuarios.values():

            if self.nombre != x:
                return False
            elif self.nombre == x:
                return True

        return None


    def verificar_pass(self):
        for x in usuarios.values():

            if self.passw != x:
                return False
            elif self.passw == x:
                return True

        return None
def verificar_gmail(gmail):
    if "@gmail.com" not in gmail:
        return False
    else:
        return True

class Login(Nombre,Password):
    def __init__(self,_nombre,_password):
        Nombre.__init__(self, _nombre)
        Password.__init__(self, _password)




class Register(Nombre,Password,Gmail,Edad):
    def __init__(self,_nombre,_edad,_gmail,_password,_id):

        Nombre.__init__(self, _nombre)
        Edad.__init__(self,_edad)
        Gmail.__init__(self,_gmail)
        Password.__init__(self, _password)
        self.id = _id

    def __repr__(self):
        return f"id"

