from LogicaUsuarios import Nombre,Password,Gmail,Edad


class Login(Nombre,Password):
    def __init__(self,_nombre,_password):
        Nombre.__init__(self, _nombre)
        Password.__init__(self, _password)

    def saludar(self):
        print(f"Hola {self.nombre}, contraseña: {self.passw}")


class Register(Nombre,Password,Gmail,Edad):
    def __init__(self,_nombre,_edad,_gmail,_password,_id):

        Nombre.__init__(self, _nombre)
        Edad.__init__(self,_edad)
        Gmail.__init__(self,_gmail)
        Password.__init__(self, _password)
        self.id = _id

    def __repr__(self):
        return f"id"

def verificar_pass():
    pass


def verificar_nombre():
    pass

def verificar_gmail(gmail):
    if "@gmail.com" not in gmail:
        return False
    else:
        return True
