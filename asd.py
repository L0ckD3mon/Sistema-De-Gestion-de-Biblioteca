from LogicaUsuarios import Nombre,Password,Gmail,Edad
from Usuarios import  usuarios

class Verificador(Password,Nombre):
    def __init__(self,_nombre,_passw):
        Nombre.__init__(self, _nombre)
        Password.__init__(self, _passw)

    def verificar_user(self):
        for x in usuarios.values():
            if x.get("nombre") == self.nombre and x.get("passw") == self.passw:
                return True
            else:
                return False

def verificar_gmail(gmail):
    if "@gmail.com" not in gmail:
        return False
    else:
        return True

def establecer_estado(nuevo_estado):
    estado = nuevo_estado
    return estado






class Login(Nombre,Password):
    def __init__(self,_nombre,_password):
        Nombre.__init__(self, _nombre)
        Password.__init__(self, _password)



class Register(Nombre,Password,Gmail,Edad):
    def __init__(self,_nombre,_edad,_gmail,_password,_id,_estado):

        Nombre.__init__(self, _nombre)
        Edad.__init__(self,_edad)
        Gmail.__init__(self,_gmail)
        Password.__init__(self, _password)
        self.estado = _estado
        self.id = _id

    def __repr__(self):
        return f"id"

