usuarios = {}
id = 0
id_dicc = -1
from LogicaUsuarios import Nombre,Password,Gmail,Edad

class Almacenar_Datos_Registro(Nombre,Password,Gmail,Edad):
    def __init__(self,_nombre,_edad,_gmail,_passw,_id):
        Nombre.__init__(self, _nombre)
        Edad.__init__(self,_edad)
        Gmail.__init__(self,_gmail)
        Password.__init__(self, _passw)
        self.id = _id

    def zipear(self):
        lista_base = ["nombre","edad","mail","passw","id"]
        lista = [self.nombre,self.edad,self.gmail,self.passw,self.id]
        nueva_info = zip(lista_base,lista)
        return nueva_info

